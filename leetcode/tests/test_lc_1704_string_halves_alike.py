from lc_1704_string_halves_alike import Solution

def test_false():
    s = Solution()
    input = "textbook"
    assert False == s.halvesAreAlike(input)

def test_true():
    s = Solution()
    input = "tootbook"
    assert True == s.halvesAreAlike(input)
