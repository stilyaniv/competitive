class Solution:
    """
    https://leetcode.com/problems/longest-valid-parentheses/
    """
    def longestValidParentheses(self, S: str) -> int:
        stack = []
        ans = 0
        for i in range(len(S)):
            if S[i] == '(': 
                stack.append(i)
            elif not stack or S[stack[-1]] == ")":
                stack = [i]
            else:
                stack.pop()
                if stack:
                    ans = max(ans, i-stack[-1])
                else:
                    ans = max(ans, i+1)
        return ans