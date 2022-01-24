from src.leetcode.lc_91_decode_ways import Solution

import pytest


@pytest.fixture
def solution():
    return Solution()


def test_0(solution):
    assert 0 == solution.numDecodings("0")


def test_1(solution):
    assert 1 == solution.numDecodings("1")


def test_12(solution):
    assert 2 == solution.numDecodings("12")


def test_10(solution):
    assert 1 == solution.numDecodings("10")


def test_2101(solution):
    assert 1 == solution.numDecodings("2101")


def test_226(solution):
    assert 3 == solution.numDecodings("226")


def test_1201234(solution):
    assert 3 == solution.numDecodings("1201234")
