# 817. Linked List Components
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        Gset = set(G)
        curr = head
        prev = False
        count = 0
        while curr:
            if curr.val in Gset and not prev:
                count += 1
            prev = curr.val in Gset
            curr = curr.next
        return count