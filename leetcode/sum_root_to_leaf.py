from data_structures.binary_tree import TreeNode


class Solution:
    def __init__(self):
        self.stack: list[int] = []
        self.total: int = 0

    def add_stack(self):
        root_to_leaf = 0
        for num in self.stack:
            root_to_leaf *= 10
            root_to_leaf += num

        self.total += root_to_leaf

    def dfs(self, node: TreeNode):
        self.stack.append(node.val)

        # If at leaf
        if not node.left and not node.right:
            self.add_stack()

        if node.left:
            self.dfs(node.left)

        if node.right:
            self.dfs(node.right)

        self.stack.pop()

    def sumNumbers(self, root: TreeNode) -> int:
        self.dfs(root)

        return self.total
