class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == '__main__':
    p = Treenode(3)
    p.left = Treenode(1)
    p.right = Treenode(2)
    p.left.left = Treenode(1)
    p.left.right = Treenode(0)
    p.right.left = Treenode(1)
    p.right.right = Treenode (1)

    q = Treenode(3)
    q.left = Treenode(1)
    q.right = Treenode(2)
    q.left.left = Treenode(1)
    q.left.right = Treenode(0)
    q.right.left = Treenode(1)
    q.right.right = Treenode (1)
    test = Solution()
    a = test.isSameTree(p,q)
    print(a)
