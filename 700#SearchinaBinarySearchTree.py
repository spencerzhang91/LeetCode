# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == val:
                return curr
            elif curr.val < val:
                if curr.right:
                    stack.append(curr.right)
            elif curr.val > val:
                if curr.left:
                    stack.append(curr.left)
        return None