from typing import List


class Solution:
    def visitPath(self, matrix, i, j):
        if i >= len(matrix) or i < 0 or j < 0 or j >= len(matrix[i]):
            return 0

        return (
            1
            + self.visitPath(matrix, i + 1, j + 1)
            + self.visitPath(matrix, i + 1, j - 1)
            + self.visitPath(matrix, i - 1, j + 1)
            + self.visitPath(matrix, i - 1, j - 1)
        )

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        return self.visitPath(matrix, 0, 0)


if __name__ == "__main__":
    s = Solution()
    assert 1 == s.longestIncreasingPath([[1]])
    assert 4 == s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
