from linked_list import ListNode

class Solution:
    def hasCycle(self, head: ListNode|None) -> bool:
        if not head or not head.next: return False

        slow = head
        fast = head.next

        while True:
            if not fast: return False
            if slow == fast: return True

            slow = slow.next
            fast = fast.next

            if not fast: return False
            if slow == fast: return True

            fast = fast.next