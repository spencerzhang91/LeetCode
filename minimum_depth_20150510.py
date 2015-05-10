class Solution:
    # @param {Treenode} root
    # @return {integer}
    def minDepth(self, root):
        depth = 0
        if root != None:
            depth += 1
            self.minDepth(root.left)
            self.minDepth(root.right)
        else:
            return depth

class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    p = Treenode(3)
    p.left = Treenode(1)
    p.right = Treenode(2)
    p.left.left = Treenode(1)
    p.left.right = Treenode(0)
    p.right.left = Treenode(1)
    

    test = Solution()
    print(test.minDepth(p))
