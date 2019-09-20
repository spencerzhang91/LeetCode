"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from typing import List

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(node):
            if node:
                for child in node.children:
                    traverse(child)
                self.res.append(node.val)
        self.res = []
        traverse(root)
        return self.res


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution2:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)
        return res[::-1]
