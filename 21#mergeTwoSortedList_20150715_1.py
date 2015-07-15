# including testing code
# need to be simplified
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "[%s --> %s]" % (self.val, self.next)

    def __str__(self):
        return str(self.val)

    def traverse(self):
        rec = []
        while self:
            rec.append(self.val)
            self = self.next
        print(rec)


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        curr = head
        try:
            print("curr: %d" % curr.val)
            print("l1: %d || l2: %d" % (l1.val, l2.val))
        except AttributeError:
            print("AttributeError")
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
            # test code
            try:
                print("l1: %d || l2: %d" % (l1.val, l2.val))
            except AttributeError:
                break
        if not l1:
            curr.next = l2
        else:
            curr.next = l1
        return head
        



# Test code:
if __name__ == '__main__':
    
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(5)
    n3 = ListNode(9)

    m0 = ListNode(3)
    m1 = ListNode(7)
    m2 = ListNode(8)
    m3 = ListNode(9)
    m4 = ListNode(13)

    n0.next = n1; n1.next = n2; n2.next = n3
    m0.next = m1; m1.next = m2; m2.next = m3; m3.next = m4

    l1 = n0
    l2 = m0

    #l1.traverse()
    #l2.traverse()
    
    test = Solution()
    res = test.mergeTwoLists(l1, l2)
    try:
        res.traverse()
    except AttributeError:
        print(res)
