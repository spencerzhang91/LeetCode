# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        s = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if L <= node.val <= R:
                s += node.val
            if L < node.val:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
        return s

    def rangeSumBST_recur(self, root, L, R):
        def dfs(node):
            if L <= node.val <= R:
                self.s += node.val
            if L < node.val:
                dfs(node.left)
            if node.val < R:
                dfs(node.right)
        
        self.s = 0  # the key here is to save the sum in outer scope
        dfs(root)
        return self.s