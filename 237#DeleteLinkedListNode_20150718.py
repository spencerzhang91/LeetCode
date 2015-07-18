# 237 Delete Node in Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "[%s --> %s]" % (self.val, self.next)

    
class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node.next:
            temp = node.next
            node.val = temp.val
            node.next = temp.next
            


# test code
if __name__ == '__main__':
    
    n0 = ListNode('a')
    n1 = ListNode('a')
    n2 = ListNode('a')
    n3 = ListNode('a')

    n0.next = n1; n1.next = n2; n2.next = n3
    
    test = Solution()
    print(test.deleteNode(n0))
