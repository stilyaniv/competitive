from itertools import product


class Solution:
    def getPairs(self, s: str) -> list:
        """has duplicates"""
        if len(s) == 1:
            if 1 <= int(s) <= 26:
                return (s,)
            else:
                return tuple()
        if len(s) == 2:
            result = []
            if (1 <= int(s[0]) <= 26) and (1 <= int(s[1]) <= 26):
                result.append((s[0], s[1]))
            if not s.startswith("0") and (1 <= int(s) <= 26):
                result.append((s,))
            return tuple(result)
        if len(s) > 2:
            return tuple(product(self.getPairs(s[0]), self.getPairs(s[1:]))) + tuple(
                product(self.getPairs(s[:2]), self.getPairs(s[2:]))
            )

    def numDecodings(self, s: str) -> int:
        return len(list(self.getPairs(s)))
