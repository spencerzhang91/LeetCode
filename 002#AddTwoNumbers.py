# 2 Add two numbers

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
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
    
    from pyalgolib.structures.linear.linkedList import *
    
    print("Test:")
    l1 = LinkedList([1,3,5])
    l2 = LinkedList([9,8,1])
    
    sol = Solution()
    res = sol.addTwoNumbers(l1.head, l2.head)
    
    l3 = LinkedList()
    l3.sethead(res)
    l3.traverse()
    
    
