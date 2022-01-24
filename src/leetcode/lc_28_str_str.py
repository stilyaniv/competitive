class Solution:
    def str_str_builtin(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        try:
            return haystack.index(needle)
        except ValueError:
            return -1

    def str_str_custom(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        firstIndex = -1
        needleIndex = 0
        haystackIndex = 0
        while haystackIndex < len(haystack):
            if haystack[haystackIndex] == needle[needleIndex]:
                if needleIndex == 0:
                    firstIndex = haystackIndex
                needleIndex += 1
                haystackIndex += 1
                if needleIndex == len(needle):
                    return firstIndex
            else:
                needleIndex = 0
                if firstIndex == -1:
                    haystackIndex += 1
                else:
                    haystackIndex = firstIndex + 1
                    firstIndex = -1

        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        return self.str_str_custom(haystack, needle)
