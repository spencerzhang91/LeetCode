# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "[%s --> %s]" % (self.val, self.next)

# approach iterative
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        new_head = None
        while head != None:
            temp = head
            head = head.next
            temp.next = new_head
            new_head = temp
        return new_head


# approach recursive
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        temp = head.next
        new_head = self.reveseList(temp)
        head.next = None
        temp.next = head
        return new_head
