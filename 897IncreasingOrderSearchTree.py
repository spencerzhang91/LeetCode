# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# My solution:
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def traversal(node):
            if node:
                traversal(node.left)
                self.curr.right = TreeNode(node.val)
                self.curr = self.curr.right
                traversal(node.right)

        self.tree = TreeNode(None)
        self.curr = self.tree
        if root:
            traversal(root)
        return self.tree.right


# A leetcode discussion slightly better solution:
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        '''
        first extract the vals out in-order, then build a new tree
        '''
        vals = []
        self.dfs(root, vals)
        res = curr = TreeNode(None)
        for val in vals:
            curr.right = TreeNode(val)
            curr = curr.right
        return res.right

    def dfs(self, node, res):
        if not node:
            return
        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)
