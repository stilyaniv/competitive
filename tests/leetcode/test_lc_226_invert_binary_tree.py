from src.leetcode.lc_226_invert_binary_tree import Solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TODO write tree traversal for proper comparison
def test_multiple():
    s = Solution()
    input = TreeNode(2, TreeNode(1), TreeNode(3))
    expected = TreeNode(2, TreeNode(3), TreeNode(1))
    result = s.invertTree(input)
    assert Solution.to_list(expected) == Solution.to_list(result)
