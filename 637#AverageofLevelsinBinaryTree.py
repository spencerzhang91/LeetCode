# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = [node.val for node in queue]
            res.append(sum(temp) / len(temp))
            queue = [child for node in queue for child in [node.left, node.right] if child]
        return res
