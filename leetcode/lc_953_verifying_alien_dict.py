from typing import List


class Solution:

    def _areOrderedLexi(self, first, second, order):
        letter_idx_map = {letter: idx for idx, letter in enumerate(order)}
        for i in range(min(len(first), len(second))):  
            firstIdx = letter_idx_map[first[i]]
            secondIdx = letter_idx_map[second[i]]
            if firstIdx < secondIdx:
                return True
            elif firstIdx > secondIdx:
                return False

        return len(first) <= len(second)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(1, len(words)):
            if not self._areOrderedLexi(words[i-1], words[i], order):
                return False

        return True