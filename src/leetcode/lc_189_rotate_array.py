from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.rotate_with_reverse(nums, k)

    def _reverse_in_place(self, nums: List[int], lo_i: int, hi_i: int):
        hi_i -= 1
        while lo_i < hi_i:
            temp = nums[hi_i]
            nums[hi_i] = nums[lo_i]
            nums[lo_i] = temp
            lo_i += 1
            hi_i -= 1

    def rotate_with_reverse(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        self._reverse_in_place(nums, 0, len(nums))
        self._reverse_in_place(nums, 0, k)
        self._reverse_in_place(nums, k, len(nums))

    def rotate_with_gcd(self, nums: List[int], k: int) -> None:
        """
        Not implemented
        """
        raise NotImplementedError("work in progress")
        k %= len(nums)
        i = 0
        d_i = k
        i_item = nums[i]
        while 0 != d_i:
            d_i = (i + k) % (len(nums))
            temp = nums[d_i]
            nums[d_i] = i_item
            i = d_i
            i_item = temp


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, k=3)
    print(nums, [5, 6, 7, 1, 2, 3, 4])

    nums = [-1, -100, 3, 99]
    Solution().rotate(nums, k=2)
    print(nums, [3, 99, -1, -100])
