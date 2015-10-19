# 148 SortList -- O(n^2) time complexity insertion sort approach
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)
        
class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        insert, bound, movenode = None, None, None
        curr = head.next
        while curr:                               # while first of unsorted nodes is not None
            while temp != curr:                   # while last of sorted nodes doesn't overlap with curr
                if temp.val <= curr.val:
                    insert = temp
                bound = temp
                temp = temp.next
                                                  # 'bound.next is curr' at this point is implied
            movenode = curr                       # explicit reference
            curr = curr.next                      # 'bound.next is curr' now does not comply

            if head.val > movenode.val:           # corner case1: all sorted nodes's value greater than movenode
                                                  # print('first reached')
                bound.next = movenode.next        # make link: bound->curr
                movenode.next = head
                head = movenode
            elif insert is bound:                 # corner case2: curr shall stay where it was
                                                  # print('second reached')
                bound.next = movenode
            else:                                 # standard situiation
                                                  # print('third reached')
                bound.next = movenode.next        # make link: bound->curr
                movenode.next = insert.next
                insert.next = movenode

            temp = head                           # reset temp to head in next loop
            traverse(head)
            print('\n', '--'*20)
        return head


# 148 SortList -- O(nlogn) time complexity merge sort approach
# merge sort, recursively
class Solution2:
    '''
    second solution 
    '''
    def sortList(self, head):
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                pre.next = l
                l = l.next
            else:
                pre.next = r
                r = r.next
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head


def traverse(head):
    curNode = head
    while curNode != None:
        print(curNode, end=' ')
        curNode = curNode.next
