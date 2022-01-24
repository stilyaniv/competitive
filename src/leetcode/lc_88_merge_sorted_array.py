from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
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
