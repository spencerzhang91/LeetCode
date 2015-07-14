# 19 original approach
# Solution class
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        if not head.next:
            return None        
        pointer = node = prev = head        
        for i in range(1, n):
            pointer = pointer.next            
        if not pointer.next:
            head = head.next            
        else:
            pointer = pointer.next
            node = node.next
            prev.next = node            
            while pointer.next:
                pointer = pointer.next
                node = node.next
                prev = prev.next                
            prev.next = node.next
            node.next = None            
        return head

