from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            r += 1
            if nums[l] != 0:
                l += 1


if __name__ == "__main__":
    nums = [0, 2, 3, 0, 0, 6, 7]
    Solution().moveZeroes(nums)
    print(nums, [2, 3, 6, 7, 0, 0, 0])
