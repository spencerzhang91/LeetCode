# initial approach
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "[%s --> %s]" % (self.val, self.next)

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        first = []
        new = []
        p1 = head
        while p1 != None:
            first.append(p1.val)
            p1 = p1.next
        new_head = None
        while head != None:
            temp = head
            head = head.next
            temp.next = new_head
            new_head = temp
        p2 = new_head
        while p2 != None:
            new.append(p2.val)
            p2 = p2.next
        
        return first == new


# reduce time by 2 approach
class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        node = head
        cnt = 0
        while node:
            node = node.next
            cnt += 1
        node = head
        pre = None
        for i in range(cnt //2):
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        if cnt % 2 == 0:
            second_half = node
        else:
            second_half = node.next
        first_half = pre
        while first_half:
            if first_half.val != second_half.val:
                return False
            else:
                first_half = first_half.next
                second_half =second_half.next
        return True

