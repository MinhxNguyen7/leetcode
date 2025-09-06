from binary_tree import TreeNode

class Solution:
    @staticmethod
    def height_diameter(root: TreeNode|None) -> tuple[int, int]:
        """
        Returns the height and diameter of the tree, respectively
        """
        if not root: return (0, 0)

        left_height, left_diameter = Solution.height_diameter(root.left)
        right_height, right_diameter = Solution.height_diameter(root.right)

        return (
            max(left_height, right_height) + 1,
            max(
                left_diameter,
                right_diameter,
                left_height + right_height + 1
            )
        )


    def diameterOfBinaryTree(self, root: TreeNode|None) -> int:
        return Solution.height_diameter(root)[1] - 1
