from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    @classmethod
    def to_list(cls, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        return [root.val] + cls.to_string(root.left) + cls.to_string(root.right)

    @classmethod
    def from_list(cls, roots):
        # if roots:
        pass


if __name__ == "__main__":
    input = TreeNode(2, TreeNode(1), TreeNode(3))
    # input = TreeNode(1)
    result = Solution.to_string(input)
    print(result)
