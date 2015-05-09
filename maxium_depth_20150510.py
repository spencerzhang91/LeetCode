class Solution:
    # @param {Treenode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

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
    p.right.right = Treenode (1)

    test = Solution()
    print(test.maxDepth(p))
