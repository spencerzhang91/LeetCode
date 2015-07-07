class Solution:
    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return None
        temp = head.next
        new_head = reveseList(temp)
        head.next = None
        temp.next = head
        return new_head
