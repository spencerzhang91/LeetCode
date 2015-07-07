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
