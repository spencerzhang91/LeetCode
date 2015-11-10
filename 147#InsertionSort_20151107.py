#147 InsertionSort_20151107

'''
rule breaking shameless approach below:
Final correct solution will be done within 20 minutes
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next
        array.sort()
        curr = head = ListNode(0) # the temp head
        for item in array:
            temp = ListNode(item)
            curr.next = temp
            curr = curr.next
        head = head.next
        return head
            
            
# solve the 'TLE' case of LeetCode OJ            
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        pre = cursor = dummy_head = ListNode(0)
        dummy_head.next = head

        while cursor.next:
            if pre.next.val > cursor.next.val:
                pre = dummy_head

            while pre.next.val < cursor.next.val:
                pre = pre.next

            if pre != cursor:
                node = cursor.next
                cursor.next = node.next
                node.next = pre.next
                pre.next = node
            else:
                cursor = cursor.next

        return dummy_head.next

# orignal approach activate TLE case
class Solution:
    def insertionSortList1(self, head):
        pre = curr = dummy = ListNode(0)
        dummy.next = head
        while curr.next:
            pre = dummy
            while pre.next.val < curr.next.val:
                pre = pre.next
            if pre != curr:
                node = curr.next
                curr.next = node.next
                node.next = pre.next
                pre.next = node
            else:
                curr = curr.next
        return dummy.next
        
    def insertionSortList2(self, head):
        pre = curr = dummy = ListNode(0)
        dummy.next = head
        while curr.next:
            pre = dummy
            while pre != curr:
                TraversalLinkedList(dummy)
                print()
                if pre.next.val < curr.next.val:
                    pre = pre.next
                else:
                    node = curr.next
                    curr.next = node.next
                    node.next = pre.next
                    pre.next = node
            curr = curr.next
        return dummy.next
