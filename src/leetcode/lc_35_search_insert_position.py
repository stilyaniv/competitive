from typing import List


class Solution:
    """
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found. If not, return the index
    where it would be if it were inserted in order.
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if target <= nums[i]:
                return i
            i += 1
        return i
