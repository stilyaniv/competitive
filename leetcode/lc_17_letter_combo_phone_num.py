from typing import List
from itertools import product

DIGIT_TO_LETTER_MAP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz", 
}

class Solution:
    """
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        iterables = []
        for digit in digits:
            iterables.append(DIGIT_TO_LETTER_MAP[digit])
            
        return ["".join(tuple) for tuple in (product(*iterables))]