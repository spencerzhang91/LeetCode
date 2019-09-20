# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = [root]
        curr = root.val
        while stack:
            node = stack.pop()
            if node.val != curr:
                return False
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return True