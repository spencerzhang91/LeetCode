"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from typing import List

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def traversal(node):
            if not node:
                return None
            else:
                self.res.append(node.val)
                for child in node.children:
                    traversal(child)
        self.res = []
        traversal(root)
        return self.res


class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        stack = []
        result = []
        if root:
            stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            for i in range(len(curr.children)-1, -1, -1):
                stack.append(curr.children[i])
        return result
