VOWELS = set("aeiouAEIOU")

class Solution:
    def _isVowel(self, c: str) -> bool:
        return c in VOWELS
    
    def halvesAreAlike(self, s: str) -> bool:
        firstCount = 0
        secondCount = 0
        midIdx = len(s) // 2
        for i in range(midIdx):
            if self._isVowel(s[i]):
                firstCount += 1
            if self._isVowel(s[i+midIdx]):
                secondCount += 1   
        
        return firstCount == secondCount
        