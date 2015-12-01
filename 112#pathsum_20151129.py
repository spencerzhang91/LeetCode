# 112 path sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        node = root
        stack = []
        spurnode, currpath = [], []
        res = []
        while node or stack:
            while node:
                if not isLeaf(node):
                    stack.append(node)
                    currpath.append(node)
                    node = node.left
                else:
                    res.append(currpath)
                    currpath = []
                    node = root
            if stack:
                node = stack.pop()
                node = node.right
        return currpath

    def isLeaf(self, node):
        return not (node.left or node.right)


def traversal(root):
    if root:
        print(root.val, end=' ')
        traversal(root.left)
        traversal(root.right)


if __name__ == "__main__":

    tree = TreeNode(10)
    tree.left = TreeNode(3)
    tree.right = TreeNode(4)
    tree.left.right = TreeNode(20)

    traversal(tree)
    print()
    test = Solution()
    res = test.hasPathSum(tree, 33)