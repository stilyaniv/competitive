from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.merge_fast(nums1, m, nums2, n)

    def merge_fast(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[m + n + 1] = nums1[m]
                m -= 1
            else:
                nums1[m + n + 1] = nums2[n]
                n -= 1
        nums1[: n + 1] = nums2[: n + 1]

    def merge_slow(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        i = j = 0
        for i in range(len(nums1)):
            if nums1[i] > nums2[j] or (nums1[i] == 0 and i >= m + j):
                nums1.pop()
                nums1.insert(i, nums2[j])
                j += 1
            if j >= n:
                break


def test1():
    expected = [1, 2, 2, 3, 5, 6]
    nums1, m = [1, 2, 3, 0, 0, 0], 3
    nums2, n = [2, 5, 6], 3

    Solution().merge(nums1, m, nums2, n)
    try:
        assert expected == nums1
    except:
        raise Exception(nums1)


def test2():
    expected = [1, 2, 2, 3, 5, 6]
    nums1, m = [2, 5, 6, 0, 0, 0], 3
    nums2, n = [1, 2, 3], 3

    Solution().merge(nums1, m, nums2, n)
    try:
        assert expected == nums1
    except:
        raise Exception(nums1)


if __name__ == "__main__":
    # test1()
    test2()
