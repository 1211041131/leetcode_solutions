class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head

        ans = head

        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return ans 