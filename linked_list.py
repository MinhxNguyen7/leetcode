from typing import Iterable

class ListNode:
    """
    A linked list class with some helpful utilities
    """
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next
    
    @staticmethod
    def from_arr(arr: Iterable[int]) -> "ListNode|None":
        it = iter(arr)
        head = ListNode(next(it), None)
        
        node = head
        node.next = None
        
        for num in it:
            node.next = ListNode(num, None)
            node = node.next

        return head
    
    def nodes(self):
        node = self
        
        while node:
            yield node
            node = node.next
            
    def __str__(self):
        """
        WARNING: This results in an infinite loop if the linked list has a cycle
        """
        return "[" + ", ".join(str(node.val) for node in self.nodes()) + "]"