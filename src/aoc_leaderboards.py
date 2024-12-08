import datetime
import json
import logging
import os
from pathlib import Path
from pprint import pprint

import pandas as pd
import plotly.express as px
import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

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


pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

if __name__ == "__main__":
    """
    https://stackoverflow.com/questions/38231591/split-explode-a-column-of-dictionaries-into-separate-columns-with-pandas

    """
    YEAR = 2024
    download_latest()
    latest = get_latest_status(f"./scratch/aoc_{YEAR}/")

    df = pd.DataFrame.from_dict(latest["members"]).T
    df["local_score"] = df["local_score"].astype(int)
    df["stars"] = df["stars"].astype(int)

    df = df.sort_values(["local_score"], ascending=False)
    df_star_cols_norm = pd.json_normalize(df["completion_day_level"])
    df = pd.concat(
        [df.reset_index(drop=True), df_star_cols_norm],
        axis=1,
    )
    df = df.drop(["completion_day_level"], axis=1)
    df = df.loc[:, ~df.columns.str.endswith("star_index")]

    num_players = len(latest["members"])
    star_score_cols = []
    for col in df.columns:
        if col.endswith("get_star_ts"):
            ts_col = col
            df[ts_col] = pd.to_datetime(df[ts_col], unit="s")
            rank_col = ts_col.replace("get_star_ts", "daily_rank")
            df[rank_col] = (
                df[ts_col].rank(na_option="bottom", ascending=True).astype(int)
            )
            star_score_col = ts_col.replace("get_star_ts", "star_score")
            df[star_score_col] = num_players + 1 - df[rank_col]
            df.loc[df[ts_col].isna(), star_score_col] = 0
            star_score_cols.append(star_score_col)
    star_score_cols = sorted(star_score_cols)
    df["local_rank"] = (
        df["local_score"]
        .rank(na_option="bottom", method="min", ascending=False)
        .astype(int)
    )

    df = df.sort_values(["local_score"], ascending=False).reset_index(drop=True)

    print(df)

    if AOC_MEMBER_ID:
        user = latest["members"][AOC_MEMBER_ID]
        current_user_name = user["name"]
        print(f"Last star TS: {datetime.datetime.fromtimestamp(user['last_star_ts'])}")

    df["calculated_score"] = df.loc[:, star_score_cols].sum(axis=1)
    try:
        assert (df["local_score"] == df["calculated_score"]).all()
    except AssertionError:
        logger.error(
            "The chart may be showing incorrect daily scores as the scores from the API do not match the calculated scores. This is likely due to a mismatch between the scoring algorithms of this program and AoC."
        )

    day1_ts = latest["day1_ts"]
    print(f"Day 1: {datetime.datetime.fromtimestamp(day1_ts)}")

    max_score = num_players * len(star_score_cols)
    print(f"Number of players: {num_players}")
    print(f"Max score: {max_score}")

    df["name_with_score"] = (
        df["local_rank"].astype(str)
        + ") "
        + df["name"]
        + " ★ "
        + df["local_score"].astype(str)
    )

    if current_user_name:
        df.loc[df["name"] == current_user_name, ["name_with_score"]] = (
            df.loc[df["name"] == current_user_name, ["name_with_score"]] + " ⭐"
        )

    fig = px.bar(
        df,
        x="name_with_score",
        y=sorted(star_score_cols),
        labels={
            "name_with_score": "Participant and total score",
            "value": "Score per star",
        },
    )
    fig.show()
