from linked_list import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode|None, l2: ListNode|None) -> ListNode|None:
        carry = 0
        head: ListNode|None = None
        prev: ListNode|None = None

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, digit = divmod(val1 + val2  + carry, 10)

            node = ListNode(digit)
            if prev:
                prev.next = node
            else:
                head = node
            prev = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            node = ListNode(1)
            if prev:
                prev.next = node

        return head

if __name__ == '__main__':
    print(Solution().addTwoNumbers(
        ListNode.from_arr([2, 4, 3]), 
        ListNode.from_arr([5, 6, 4])
    ))