# 102 Binary Tree Level Order Traversal
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        currlevel, nextlevel = [root], []      # for tracking the tree nodes
        currvals, nextvals = [root.val], []    # for recording tree node values
        result = []                            # final result
        while currlevel:
            for item in currlevel:
                if item.left:
                    nextlevel.append(item.left)
                    nextvals.append(item.left.val)
                if item.right:
                    nextlevel.append(item.right)
                    nextvals.append(item.right.val)
            result.append(currvals)
            currlevel = nextlevel
            currvals = nextvals
            nextlevel = []
            nextvals = []
        return result


                            
        
        
