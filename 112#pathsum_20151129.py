# 112 path sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum1(self, root, s):
        """
        recursive approach
        """
        if not root:
            return False
        if not (root.left or root.right):
            if root.val == s:
                return True
        return (self.hasPathSum(root.left, s-root.val) 
                or self.hasPathSum(root.right, s-root.val))

    def hasPathSum2(self, root, s):
        """
        iterative dfs approach
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, curs = stack.pop()
            if not (node.left or node.right):
                if curs == s:
                    return True
            if node.left:
                stack.append((node.left, curs + node.left.val))
            if node.right:
                stack.append((node.right, curs + node.right.val))
        return False


if __name__ == "__main__":

    tree = TreeNode(10)
    tree.left = TreeNode(3)
    tree.right = TreeNode(4)
    tree.left.right = TreeNode(20)