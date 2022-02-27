from typing import List
from collections import deque


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        li = 0
        ri = len(nums) - 1
        sorted_nums = deque()
        while li <= ri:
            left = nums[li] ** 2
            right = nums[ri] ** 2
            if left > right:
                sorted_nums.appendleft(left)
                li += 1
            elif right >= left:
                sorted_nums.appendleft(right)
                ri -= 1
        return list(sorted_nums)


if __name__ == "__main__":
    print(Solution().sortedSquares(nums=[-4, -1, 0, 3, 10]))
    print([0, 1, 9, 16, 100])
