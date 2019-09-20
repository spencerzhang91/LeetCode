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