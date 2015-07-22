# 83 remove duplicates from sorted list

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        pre = cur = head
        while cur:
            while cur and pre.val == cur.val:
                cur = cur.next
                pre.next = cur
            pre = cur
            if cur:
                cur = cur.next
        return head

