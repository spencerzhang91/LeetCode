# 112 path sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        recursive approach
        """
        if not root:
            return False
        if not (root.left or root.right):
            if root.val == sum:
                return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


if __name__ == "__main__":

    tree = TreeNode(10)
    tree.left = TreeNode(3)
    tree.right = TreeNode(4)
    tree.left.right = TreeNode(20)

    traversal(tree)