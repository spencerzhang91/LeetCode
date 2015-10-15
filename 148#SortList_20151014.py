# 148 SortList -- O(n^2) time complexity insertion sort approach
# Definition for singly-linked list.
class ListNode(object):
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
            print('\n','--'*20)
        return head

def traverse(head):
    curNode = head
    while curNode != None:
        print(curNode, end=' ')
        curNode = curNode.next

        
if __name__ == "__main__":
	node1 = ListNode(6)
	node2 = ListNode(2)
	node3 = ListNode(11)
	node4 = ListNode(6)
	node5 = ListNode(7)
	node1.next = node2; node2.next = node3
	node3.next = node4; node4.next = node5
	# traverse(node1)
	test = Solution()
	test.sortList(node1)