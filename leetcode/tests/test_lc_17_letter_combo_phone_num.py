from lc_17_letter_combo_phone_num import Solution

def test_multiple():
    s = Solution()
    expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert expected == s.letterCombinations("23")

def test_single():
    s = Solution()
    expected = ["a","b","c"]
    assert expected == s.letterCombinations("2")

def test_empty():
    s = Solution()
    expected = []
    assert expected == s.letterCombinations("")