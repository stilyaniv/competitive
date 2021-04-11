from src.leetcode.lc_953_verifying_alien_dict import Solution


def test_identical():
    s = Solution()
    assert True == s.isAlienSorted(["hello", "hello"], "hlabcdefgijkmnopqrstuvwxyz")


def test_simple():
    s = Solution()
    assert True == s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")


def test_multiple():
    s = Solution()
    assert False == s.isAlienSorted(
        ["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"
    )

def test_same_root():
    s = Solution()
    assert False == s.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz")
