class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        if not root: return []
        L = []
        stack = []
        lastvisited = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and lastvisited != peek.right:
                    root = peek.right
                else:
                    L.append(peek.val)
                    lastvisited = stack.pop()
        return L

if __name__ == "__main__":
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('c')
    root.left.left = TreeNode('d')
    root.left.right = TreeNode('d')

    test = Solution()
    print(test.postorderTraversal(root))
