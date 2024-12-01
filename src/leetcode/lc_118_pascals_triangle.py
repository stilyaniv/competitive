from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t = []
        for n in range(numRows):
            t.append([])
            for m in range(n + 1):
                if m == 0 or m == n:
                    t[n].append(1)
                else:
                    num = t[n - 1][m] + t[n - 1][m - 1]
                    t[n].append(num)
        return t


def test1():
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]
    numRows = 5
    res = Solution().generate(numRows)
    try:
        assert expected == res
    except:
        raise Exception(f"\n{res} should be\n{expected}")


if __name__ == "__main__":
    test1()
