class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node|None" = None,
        right: "Node|None" = None,
        next: "Node|None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    @staticmethod
    def find_child_next(parent: Node | None) -> Node | None:
        """
        Searches the current level, starting from the given node, for the first child.
        Returns that child if it exists.
        """
        current = parent
        while current:
            if current.left:
                return current.left

            if current.right:
                return current.right

            current = current.next

        return None

    @staticmethod
    def link_children(parent: Node) -> Node | None:
        """
        Populate the `next` reference for the given node's children and return
        the left-most child, if any.
        """
        left = parent.left
        right = parent.right

        next_child = Solution.find_child_next(parent.next)

        if left and right:
            left.next = right
            right.next = next_child
            return left

        if left and not right:
            left.next = next_child
            return left

        if not left and right:
            right.next = next_child
            return right

        # No children
        return None

    def connect(self, root: "Node|None") -> "Node|None":
        next_left = root
        while next_left:
            current = next_left
            next_left = None

            # Explore and link nodes in next layer
            while current:
                leftmost_child = Solution.link_children(current)
                next_left = next_left or leftmost_child
                current = current.next

        return root
