"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q, level = root and [root], 0
        while q:
            q = [child for node in q for child in node.children if child]
            level += 1
        return level


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        else:
            return max([self.maxDepth(child) for child in root.children]) + 1

