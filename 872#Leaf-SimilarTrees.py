# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.leaves1 = []
        self.leaves2 = []
        Solution.inorder(root1, self.leaves1)
        Solution.inorder(root2, self.leaves2)
        return self.leaves1 == self.leaves2
    
    def inorder(node, leaves):
        if node:
            Solution.inorder(node.left, leaves)
            if not node.left and not node.right:
                leaves.append(node.val)
            Solution.inorder(node.right, leaves)