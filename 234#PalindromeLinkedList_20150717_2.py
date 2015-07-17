# reduce time by 2 approach
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
            
                


# test code
if __name__ == '__main__':
    
    n0 = ListNode('a')
    n1 = ListNode('a')
    n2 = ListNode('a')
    n3 = ListNode('a')

    n0.next = n1; n1.next = n2; n2.next = n3
    
    test = Solution()
    print(test.isPalindrome(n0))
