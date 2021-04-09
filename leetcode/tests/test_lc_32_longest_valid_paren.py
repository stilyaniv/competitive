from lc_32_longest_valid_paren import Solution

def test_empty():
    s = Solution()
    assert 0 == s.longestValidParentheses("")

def test_simple_closed_start_():
    s = Solution()
    assert 2 == s.longestValidParentheses(")()")

def test_simple_open_start():
    s = Solution()
    assert 2 == s.longestValidParentheses("(()")

def test_interrupted_open():
    s = Solution()
    assert 2 == s.longestValidParentheses("()(()(")

def test_interrupted_closed():
    s = Solution()
    assert 2 == s.longestValidParentheses("())()(")

def test_remaining_open():
    s = Solution()
    assert 4 == s.longestValidParentheses("(()()(")

def test_remaining_closed():
    s = Solution()
    assert 4 == s.longestValidParentheses(")()())")

def test_nested():
    s = Solution()
    assert 6 == s.longestValidParentheses("()(())")

def test_consecutive_open():
    s = Solution()
    assert 4 == s.longestValidParentheses("(())(((())")

def test_consecutive_closed():
    s = Solution()
    assert 4 == s.longestValidParentheses("(())))(())")

