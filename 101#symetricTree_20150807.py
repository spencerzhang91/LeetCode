# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root:
            return self.compare(root.left, root.right)
        return True

    def compare(self, left, right):
        if left == None or right == None:
            if left == None and right == None:
                return True
            else:
                return False
        else:
            if left.val != right.val:
                return False
            return self.compare(left.left, right.right) and\
                   self.compare(left.right, right.left)

