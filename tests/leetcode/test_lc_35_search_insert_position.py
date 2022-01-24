from src.leetcode.lc_35_search_insert_position import Solution

import pytest


@pytest.fixture
def solution():
    return Solution()


def test_search_insert_position_example_1(solution):
    assert 2 == solution.searchInsert([1, 3, 5, 6], 5)


def test_search_insert_position_example_2(solution):
    assert 1 == solution.searchInsert([1, 3, 5, 6], 2)


def test_search_insert_position_example_3(solution):
    assert 4 == solution.searchInsert([1, 3, 5, 6], 7)


def test_search_insert_position_example_4(solution):
    assert 0 == solution.searchInsert([1, 3, 5, 6], 0)


def test_search_insert_position_example_5(solution):
    assert 0 == solution.searchInsert([1], 0)
