# 19 simplified approach
# Solution class
class Solution:
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None
        p1 = p2 = head
        for i in range(n):
            p2 = p2.next
        if not p2:
            return head.next
        while p2 and p2.next != None:
            p2 = p2.next
            p1 = p1.next
        if p1.next:
            p1.next = p1.next.next
            return head
        else:
            return None
