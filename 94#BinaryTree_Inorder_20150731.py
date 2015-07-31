class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        res = []
        self.recursive(root, res)
        return res

    def recursive(self, root, res):
        if root:
            self.recursive(root.left, res)
            res.append(root.val)
            self.recursive(root.right, res)

if __name__ == "__main__":
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('c')
    root.left.left = TreeNode('d')
    root.left.right = TreeNode('d')

    test = Solution()
    print(test.preorderTraversal(root))
