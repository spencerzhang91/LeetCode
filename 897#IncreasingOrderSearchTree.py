# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = [root]
        new_tree = TreeNode(root.val)
        curr = root
        while stack:
            if curr:
