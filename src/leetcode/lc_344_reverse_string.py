import numbers
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseStringTwoPointers(s)

    def reverseStringTwoPointers(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverseStringRecursive(self, s: List[str]) -> None:
        def reverse(s, l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(s, l + 1, r - 1)

        reverse(s, 0, len(s) - 1)


if __name__ == "__main__":
    s = ["a", "b", "c"]
    Solution().reverseString(s)
    assert ["c", "b", "a"] == s

    s = ["a", "b", "c", "d"]
    Solution().reverseString(s)
    assert ["d", "c", "b", "a"] == s

    s = ["a"]
    Solution().reverseString(s)
    assert ["a"] == s

    import timeit

    run_time = timeit.timeit(
        "Solution().reverseString(['a']*(10**7))",
        setup="from __main__ import Solution",
        number=1,
    )

    print(run_time)
