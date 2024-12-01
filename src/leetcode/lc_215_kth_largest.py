from typing import List


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return left
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        top_k = []
        for i, num in enumerate(nums):
            exists = False
            i = binarySearch(top_k, num)

            if len(top_k) > k:
                top_k.pop()

            for top_i, top_num in enumerate(top_k):
                if num > top_num:
                    top_k.insert(top_i, num)
                    exists = True
                    if len(top_k) > k:
                        top_k.pop()
                    break

            if not exists and len(top_k) < k:
                top_k.append(num)

        return top_k[k - 1]

    def findKthLargest_slow(self, nums: List[int], k: int) -> int:
        top_k = []
        for i, num in enumerate(nums):
            exists = False
            for top_i, top_num in enumerate(top_k):
                if num > top_num:
                    top_k.insert(top_i, num)
                    exists = True
                    if len(top_k) > k:
                        top_k.pop()
                    break

            if not exists and len(top_k) < k:
                top_k.append(num)

        return top_k[k - 1]
