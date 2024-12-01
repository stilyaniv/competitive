from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            mid_idx = (r + l) // 2
            row_i = mid_idx // cols
            col_i = mid_idx % cols
            mid_val = matrix[row_i][col_i]
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid_idx + 1
            elif target < mid_val:
                r = mid_idx - 1
        return False


def test1():
    expected = True
    target = 3
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    res = Solution().searchMatrix(matrix, target)
    try:
        assert expected == res
    except:
        raise Exception(f"\n{res} should be\n{expected}")


def test2():
    expected = False
    target = 13
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    res = Solution().searchMatrix(matrix, target)
    try:
        assert expected == res
    except:
        raise Exception(f"\n{res} should be\n{expected}")


if __name__ == "__main__":
    test1()
    test2()
