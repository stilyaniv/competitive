from src.leetcode.lc_88_merge_sorted_array import Solution


def test_singular_insert():
    nums1, m, nums2, n = [2, 0], 1, [1], 1
    Solution().merge(nums1, m, nums2, n)
    assert [1, 2] == nums1


def test_trivial():
    nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
    Solution().merge(nums1, m, nums2, n)
    assert [1, 2, 2, 3, 5, 6] == nums1


def test_empty_destination():
    nums1, m, nums2, n = [0], 0, [1], 1
    Solution().merge(nums1, m, nums2, n)
    assert [1] == nums1


def test_sequential_inserts():
    nums1, m, nums2, n = (
        [-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        5,
        [-1, -1, 0, 0, 1, 2],
        6,
    )
    Solution().merge(nums1, m, nums2, n)
    assert [-1, -1, -1, 0, 0, 0, 0, 0, 1, 2, 3] == nums1
