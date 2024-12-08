import datetime
import json
import os
from pathlib import Path
from pprint import pprint

import pandas as pd
import plotly.express as px
import requests

AOC_URL_LEADERBOARD = os.getenv("AOC_URL_LEADERBOARD", "")
AOC_COOKIE = os.getenv("AOC_COOKIE", "")

AOC_MEMBER_ID = os.getenv("AOC_MEMBER_ID")


def download_latest():
    response = requests.get(AOC_URL_LEADERBOARD, cookies={"session": AOC_COOKIE})

    ts_now = datetime.datetime.now().isoformat()
    result_json = response.json()
    aoc_year = result_json["event"]
    owner_id = result_json["owner_id"]
    snapshots_path = f"./scratch/aoc_{aoc_year}/"
    os.makedirs(snapshots_path, exist_ok=True)
    with open(f"{snapshots_path}/private_leadboard_{owner_id}_{ts_now}.json", "w") as f:
        json.dump(result_json, f)


def get_latest_status(dir_snapshots):
    snapshots = sorted(Path(dir_snapshots).iterdir())
    latest = snapshots[-1]
    with open(latest) as f:
        latest_json = json.load(f)
    return latest_json


if __name__ == "__main__":
    """
    https://stackoverflow.com/questions/38231591/split-explode-a-column-of-dictionaries-into-separate-columns-with-pandas

    """
    YEAR = 2024
    download_latest()
    latest = get_latest_status(f"./scratch/aoc_{YEAR}/")
    if AOC_MEMBER_ID:
        user = latest["members"][AOC_MEMBER_ID]
        pprint(user, indent=2)
        print(f"Last star TS: {datetime.datetime.fromtimestamp(user['last_star_ts'])}")

    day1_ts = latest["day1_ts"]
    print(f"Day 1: {datetime.datetime.fromtimestamp(day1_ts)}")

    df = pd.DataFrame.from_dict(latest["members"]).T
    df["local_score"] = df["local_score"].astype(int)
    df["stars"] = df["stars"].astype(int)

    df = df.sort_values(["local_score"], ascending=False)
    df_star_cols_norm = pd.json_normalize(df["completion_day_level"])
    df = pd.concat(
        [df.reset_index(drop=True), df_star_cols_norm],
        axis=1,
    )

    df = df.loc[:, ~df.columns.str.endswith("star_index")]

    rank_column_names = []
    for col in df.columns:
        if col.endswith("get_star_ts"):
            rank_name = col.replace("get_star_ts", "rank")
            df[rank_name] = df[col].rank(ascending=False)
            rank_column_names.append(rank_name)
    df = df.drop(["completion_day_level"], axis=1)
    # pd.to_datetime(df['1.1.get_star_ts'], unit='s')

    participants = len(latest["members"])
    print(f"Participants: {participants}")
    print(f"Max score: {participants*len(rank_column_names)}")

    df = df.sort_values(["local_score"], ascending=False)
    fig = px.bar(df, x="name", y=sorted(rank_column_names))
    fig.show()

    # TODO create bump chart with parallel_coordinates
    # Load the iris dataset provided by the library
    # df = px.data.iris()

    # Create the chart:
    # fig = px.parallel_coordinates(
    #     df,
    #     color="local_score",
    #     # labels={"last_star_ts": "last_star_ts", "stars": "stars", "local_score": "local_score"},
    #     dimensions=['last_star_ts', 'stars'],
    #     # labels={"species_id": "Species", "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
    #     #         "petal_width": "Petal Width", "petal_length": "Petal Length", },
    #     color_continuous_scale=px.colors.diverging.Tealrose,
    #     color_continuous_midpoint=2
    # )

    # # Hide the color scale that is useless in this case
    # fig.update_layout(coloraxis_showscale=False)

    # # Show the plot
    # fig.show()
