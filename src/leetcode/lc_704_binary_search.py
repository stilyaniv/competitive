from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid_idx = start + (end - start) // 2
            mid_item = nums[mid_idx]
            if target == mid_item:
                return mid_idx
            elif target < mid_item:
                end = mid_idx - 1
            elif mid_item < target:
                start = mid_idx + 1

        return -1


if __name__ == "__main__":
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9), 4)
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=5), 3)
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=12), 5)
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2), -1)
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=13), -1)
