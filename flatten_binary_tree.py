from data_structures.binary_tree import TreeNode


class Solution:
    def flatten(
        self, root: TreeNode | None, child: TreeNode | None = None
    ) -> TreeNode | None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return child

        right_flattened = self.flatten(root.right, child) if root.right else child
        root.right = self.flatten(root.left, right_flattened)
        root.left = None

        return root
        