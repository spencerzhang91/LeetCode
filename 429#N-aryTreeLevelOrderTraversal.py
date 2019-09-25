"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = [node.val for node in queue]
            res.append(temp)
            queue = [child for node in queue for child in node.children if child]
        return res
