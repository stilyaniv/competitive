from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.hasDuplicatesSet(nums)

    def hasDuplicatesHash(self, nums: List[int]) -> bool:
        """Slower than using a set, faster with check instead of try/except"""
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

            if d[num] > 1:
                return True

        return False

    def hasDuplicatesSet(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


TIMEIT_LOCAL_SETUP = "from __main__ import Solution;s=Solution()"
TIMEIT_REPEATS = 3

if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3, 1]
    assert s.hasDuplicatesHash(nums)
    assert s.hasDuplicatesSet(nums)

    nums = [1, 2, 3, 4]
    assert not s.hasDuplicatesHash(nums)
    assert not s.hasDuplicatesSet(nums)

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert s.hasDuplicatesHash(nums)
    assert s.hasDuplicatesSet(nums)

    import timeit

    uniq = "list(range(10**4))"
    print(
        timeit.timeit(
            f"s.hasDuplicatesHash({uniq})",
            setup=TIMEIT_LOCAL_SETUP,
            number=TIMEIT_REPEATS,
        )
    )
    print(
        timeit.timeit(
            f"s.hasDuplicatesSet({uniq})",
            setup=TIMEIT_LOCAL_SETUP,
            number=TIMEIT_REPEATS,
        )
    )

    one_dup = "list(range(10 ** 4)) + [0]"
    print(
        timeit.timeit(
            f"s.hasDuplicatesHash({one_dup})",
            setup=TIMEIT_LOCAL_SETUP,
            number=TIMEIT_REPEATS,
        )
    )
    print(
        timeit.timeit(
            f"s.hasDuplicatesSet({one_dup})",
            setup=TIMEIT_LOCAL_SETUP,
            number=TIMEIT_REPEATS,
        )
    )
