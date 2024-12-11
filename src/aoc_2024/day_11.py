"""
https://adventofcode.com/
"""  # TODO link to problem

# import functools
import io
from functools import lru_cache, wraps
from pathlib import Path
from time import time
from typing import Dict, List

INPUT_FILE_PATH = f"{Path(__file__).parent}/inputs/{Path(__file__).stem}.txt"

EXAMPLE = """125 17"""

PART1_EXAMPLE_OUTPUT = 55312
PART1_OUTPUT = 183248
PART2_OUTPUT = 218811774248729


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' %
              (f.__name__, args, kw, te - ts))
        return result
    return wrap

# TODO rewrite with custom cache implementation


@lru_cache(maxsize=8192)
def splitr(stones, blinks) -> int:
    if blinks == 0:
        return len(stones)

    new_stones = 0
    for i, stone in enumerate(stones):
        stone_str = str(stone)
        size = len(stone_str)
        if stone == 0:
            new_stones = new_stones + splitr(tuple([1]), blinks - 1)
        elif size % 2 == 0:
            left = stone_str[:size // 2]
            right = stone_str[size // 2:]
            new_stones = new_stones + splitr(tuple([int(left), int(right)]), blinks - 1)
        else:
            new_stones = new_stones + splitr(tuple([stone * 2024]), blinks - 1)

    return new_stones


@timing
def part_1(file):
    stones = tuple(int(stone) for stone in file.readline().split())

    final_size = splitr(stones, 25)

    return final_size


@timing
def part_2(file):
    stones = tuple(int(stone) for stone in file.readline().split())

    final_size = splitr(stones, 75)

    return final_size


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(f"{part_1(f)} == {PART1_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(f"{part_1(f)} == {PART2_OUTPUT}?")
