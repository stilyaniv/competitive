from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)
        for l in s:
            sd[l] += 1
        for l in t:
            td[l] += 1

        if len(sd) != len(td):
            return False

        for l in td:
            if td[l] != sd.get(l):
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("aab", "baa")
    assert s.isAnagram("a", "a")
    assert s.isAnagram("abc", "cba")
    assert not s.isAnagram("abc", "abcd")
    assert not s.isAnagram("abcd", "abc")
    assert not s.isAnagram("abb", "ab")
    assert not s.isAnagram("ab", "abb")
    assert not s.isAnagram("abd", "abc")
    assert not s.isAnagram("abc", "abd")
