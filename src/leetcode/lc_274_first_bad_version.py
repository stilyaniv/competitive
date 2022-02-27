1  # The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n, func):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end, min_bad = n
        while start <= end:
            mid = start + (end - start) // 2
            if func(mid):
                min_bad = min(min_bad, mid)
                end = mid - 1
            else:
                start = mid + 1

        return start


if __name__ == "__main__":
    last_version = 10
    for i in range(1, last_version + 1):
        result = Solution().firstBadVersion(last_version, lambda x: x >= i)
        assert i == result, "Expectet: {}, result: {}".format(i, result)

    # import sys
    # print(Solution().firstBadVersion(sys.maxsize, lambda x: x >= sys.maxsize // 3))
