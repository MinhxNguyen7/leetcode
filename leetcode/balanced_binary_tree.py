from binary_tree import TreeNode

class Solution:
    @staticmethod
    def height_and_balance(root) -> int:
        """
        Returns the tree's height if it's balanced and -1 if it's not
        """
        if not root: return 0 

        left_balance = Solution.height_and_balance(root.left)
        if left_balance == -1: return -1
        
        right_balance = Solution.height_and_balance(root.right)
        if right_balance == -1: return -1

        if abs(left_balance - right_balance) > 1: return -1

        return max(left_balance, right_balance) + 1


    def isBalanced(self, root: TreeNode|None) -> bool:
        return Solution.height_and_balance(root) != -1
