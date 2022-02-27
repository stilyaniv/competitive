from typing import List


class Solution:
    """
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found. If not, return the index
    where it would be if it were inserted in order.

    Solution:
        When object isn't found, we return start because in the last loop
        start <= end and:
            if target > mid element, we place it at mid+1
            if target < mid element, we place it at mid
        which is exactly what happens to the start variable
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return start


if __name__ == "__main__":
    assert 2 == Solution().searchInsert(nums=[1, 3, 5, 6], target=5)
    assert 1 == Solution().searchInsert(nums=[1, 3, 5, 6], target=2)
    assert 4 == Solution().searchInsert(nums=[1, 3, 5, 6], target=7)
