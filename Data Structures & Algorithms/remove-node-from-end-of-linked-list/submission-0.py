class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = head

        # Move right n steps ahead
        for _ in range(n):
            right = right.next

        # Move both pointers
        while right:
            left = left.next
            right = right.next

        # Remove node
        left.next = left.next.next

        return dummy.next