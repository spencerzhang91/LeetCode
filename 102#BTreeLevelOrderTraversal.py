# 102 Binary Tree Level Order Traversal
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

def CreateBTree(infoset):
    '''
    Take a tuple contains binary tree structure information as
    argument, construct tree recursively and return the root.
    '''
    # print('infoset:', infoset)
    if infoset:
        try:
            root, leftsub, rightsub = infoset
        except ValueError:
            root = infoset[0]
            leftsub = None
            rightsub = None
    else:
        return None
    root = TreeNode(root)
    if not root:
        return None
    else:
        root.left = CreateBTree(leftsub)
        root.right = CreateBTree(rightsub)
    return root

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        currlevel = [root]
        currvals, nextvals = [root.val], []
        nextlevel, result = [], []
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


tree = ('a', ('b', ('c', 'e', ('f',None,('h','i',None))), ('d',None,'g')), None)
testroot = CreateBTree(tree)
print(testroot)
test = Solution()
res = test.levelOrder(testroot)
print(res)

                            
        
        
