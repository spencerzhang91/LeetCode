# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "[%s --> %s]" % (self.val, self.next)

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        new_head = None
        while head != None:
            temp = head
            print('temp:', temp)
            head = head.next
            print('head:', head)
            temp.next = new_head
            print('temp.next:', temp.next)
            new_head = temp
            print('temp.next:', temp.next)
        print("\n")
        return new_head

# test code
if __name__ == '__main__':
    
    n0 = ListNode('a')
    n1 = ListNode('b')
    n2 = ListNode('c')
    n3 = ListNode('d')

    n0.next = n1; n1.next = n2; n2.next = n3
    
    test = Solution()
    print(test.reverseList(n0))
