from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSumBrute(nums, target)

    def twoSumBrute(self, nums: List[int], target: int) -> List[int]:
        """ n^2 """
        for i in range(len(nums)):
            difference = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == difference:
                    return [i, j]

    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        """ O(n) - hash lookups are constant in the avg case """
        visited = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in visited:
                return [visited[difference], i]
            else:
                visited[num] = i
