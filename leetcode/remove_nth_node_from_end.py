class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head

        for _ in range(n):
            right = right.next
        
        # List size == n
        if not right:
            return head.next
        
        right = right.next

        while right:
            right = right.next
            left = left.next

        if left.next:
            left.next = left.next.next

        return head