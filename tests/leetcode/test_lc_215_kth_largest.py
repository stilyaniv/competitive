from src.leetcode.lc_215_kth_largest import Solution

# from tests.leetcode.test_lc_215_kth_largest_constants import INPUT1


def test_1():
    s = Solution()
    input = [3, 2, 1, 5, 6, 4], 2
    assert 5 == s.findKthLargest(*input)


def test_2():
    s = Solution()
    input = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    assert 4 == s.findKthLargest(*input)


def test_3():
    with open("./tests/leetcode/test_lc_215_inputs.txt") as f:
        INPUT1 = [int(num) for num in f.read().split(",")]
    s = Solution()
    input = (INPUT1, 15952)
    assert -115 == s.findKthLargest(*input)
