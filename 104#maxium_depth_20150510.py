class Solution:
    # @param {Treenode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return max(1 + self.maxDepth(root.left),
             1 + self.maxDepth(root.right))

