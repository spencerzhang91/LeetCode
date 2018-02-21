# 2 Add two numbers

# Definition for singly-linked list.
from . import pyalgolib

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = head = ListNode(l1.val + l2.val)
        while l1.next and l2.next:
            cur.val = l1.val + l2.val
            cur.next = ListNode(0)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        cur.val = l1.val + l2.val
        if l1.next is None:
            cur.next = l2.next
        elif l2.next is None:
            cur.next = l1.next
        cur = head
        while cur:
            if cur.val >= 10:
                cur.val -= 10
                if cur.next:
                    cur.next.val += 1
                else:
                    cur.next = ListNode(1)
            cur = cur.next
        return head
    
if __name__ == "__main__":
    print("Test:")
    
