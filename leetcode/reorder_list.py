from linked_list import ListNode

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr: list[ListNode] = []
        node = head
        while node:
            arr.append(node)
            node = node.next

        left = 0
        right = len(arr) - 1
        
        while left < right:
            arr[left].next = arr[right]
            
            if right == left + 1:
                break

            arr[right].next = arr[left + 1]

            left += 1
            right -= 1
        
        arr[right].next = None
            
if __name__ == '__main__':
    ll = ListNode.from_arr([1, 2, 3, 4, 5])
    Solution().reorderList(ll)
    print(ll)