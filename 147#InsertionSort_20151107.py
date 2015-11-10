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
            
                
        
    
