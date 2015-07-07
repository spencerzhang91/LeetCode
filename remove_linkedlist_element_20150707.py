# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "[%s --> %s]" % (self.val, self.next)

    def __str__(self):
        return self.val

# Travese function
def traverse(head):
    curNode = head
    while curNode != None:
        print(curNode)
        curNode = curNode.next

# Solution class
class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, target):
        prev = None
        curr = head
        while curr is not None:
            if curr.val != target:
                prev = curr
                curr = curr.next
            else:
                if curr is head:
                    head = curr.next
                else:
                    prev.next = curr.next
                curr = curr.next
        return head #Have to return head to pass the OJ


# Test code:
if __name__ == '__main__':
    
    n0 = ListNode('a')
    n1 = ListNode('a')
    n2 = ListNode('b')
    n3 = ListNode('c')

    n0.next = n1; n1.next = n2; n2.next = n3
    head = n0
    
    test = Solution()
    test.removeElements(head, 'd')
    #traverse(head)
    
