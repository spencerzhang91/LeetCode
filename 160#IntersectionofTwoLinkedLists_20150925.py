# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB
        cnta, cntb = 0, 0
        while pa:
            pa = pa.next
            cnta += 1
        while pb:
            pb = pb.next
            cntb += 1
        if cnta > cntb:
            for i in range(cnta - cntb):
                headA = headA.next
        else:
            for i in range(cntb - cnta):
                headB = headB.next
        while not (headA is headB):
            headA = headA.next
            headB = headB.next
        return headA
