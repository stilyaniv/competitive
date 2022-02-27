from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        return self.reverseWordsTwoFlips(s)

    def reverseString(self, s: List[str], l: int, r: int) -> None:
        r -= 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverseWordsCopy(self, s: str) -> str:
        """ Slower than reversing twice """
        return " ".join([word[::-1] for word in s.split()])

    def reverseWordsTwoFlips(self, s: str) -> str:
        """ Faster than iterating over each word"""
        return " ".join(s[::-1].split()[::-1])

    def reverseWordsInPlace(self, s: str) -> None:
        """This becomes inneficient in py - converting from string to
        list of chars and back to string creates new objects.
        """
        reversed_string = ""
        charList = list(s)
        l, r = 0, 1
        while r < len(charList):
            if charList[r] == " ":
                word = charList[l:r]
                self.reverseString(word, 0, len(word))
                for char in word:
                    reversed_string += char
                reversed_string += " "
                l = r + 1
                r = r + 2
            else:
                r += 1

        word = charList[l:r]
        self.reverseString(word, 0, len(word))
        for char in word:
            reversed_string += char

        return reversed_string


if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))
    print("s'teL ekat edoCteeL tsetnoc")

    import timeit

    timeit_rerun_count = 5

    # run_time = timeit.timeit(
    #     "Solution().reverseWordsInPlace('a'*(10**7))",
    #     setup="from __main__ import Solution",
    #     number=timeit_rerun_count,
    # )
    # print(run_time)

    run_time = timeit.timeit(
        "Solution().reverseWordsCopy('b'*(10**7))",
        setup="from __main__ import Solution",
        number=timeit_rerun_count,
    )
    print(run_time)

    run_time = timeit.timeit(
        "Solution().reverseWordsTwoFlips('b'*(10**7))",
        setup="from __main__ import Solution",
        number=timeit_rerun_count,
    )
    print(run_time)
