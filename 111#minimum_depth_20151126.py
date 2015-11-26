# 111 minimum depth of binary tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        upper_queue = [root]
        lower_queue = []
        depth = 1
        while upper_queue:
            for node in upper_queue:
                if (node.left or node.right):
                    if node.left: lower_queue.append(node.left)
                    if node.right: lower_queue.append(node.right)
                else: return depth
            depth += 1
            upper_queue = lower_queue
            lower_queue = []

            




