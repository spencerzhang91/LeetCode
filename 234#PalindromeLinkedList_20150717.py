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


# test code
if __name__ == '__main__':
    
    n0 = ListNode('a')
    n1 = ListNode('a')
    n2 = ListNode('a')
    n3 = ListNode('a')

    n0.next = n1; n1.next = n2; n2.next = n3
    
    test = Solution()
    print(test.isPalindrome(n0))
