#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 61 Rotate List
"""
Created on Thu Feb 15 18:42:12 2018

@author: spencer
"""


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        left = right = head
        for i in range(k % length):
            right = right.next
        if not right:
            return head
        while right.next:
            left = left.next
            right = right.next
        right.next = head
        new_head = left.next
        left.next = None
        return new_head
        
if __name__ == "__main__":
    
    sl = Solution()
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
            
    h = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    h.next = n1
    n1.next = n2
    n2.next = n3
    
    sl.rotateRight(h, 2)
    