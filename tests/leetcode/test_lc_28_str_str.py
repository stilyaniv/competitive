from src.leetcode.lc_28_str_str import Solution

import pytest


@pytest.fixture
def solution():
    return Solution()


def test_str_str_basic(solution):
    assert 2 == solution.str_str_custom("hello", "ll")


def test_str_str_after_similar_substring(solution):
    assert 4 == solution.str_str_custom("mississippi", "issip")


def test_at_the_end(solution):
    assert 9 == solution.str_str_custom("mississippi", "pi")
