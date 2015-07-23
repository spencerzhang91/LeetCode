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
    

# simplified approach
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

