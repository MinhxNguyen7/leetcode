from binary_tree import TreeNode

MAX_VAL = pow(2, 31)
MIN_VAL = -MAX_VAL

class Solution:
    @staticmethod
    def isValidBST(root: TreeNode|None, le = MAX_VAL, ge = MIN_VAL) -> bool:
        if root is None: return True
        
        val_in_range = ge <= root.val <= le
        
        if not val_in_range: 
            return False
        
        left_is_valid = (
            root.left is None or 
            (
                root.left.val < root.val and 
                Solution.isValidBST(root.left, le=min(le, root.val) - 1, ge=ge)
            )
        )
        
        if not left_is_valid: 
            return False
        
        right_is_valid = (
                root.right is None or 
                (
                    root.right.val > root.val and 
                    Solution.isValidBST(root.right, le=le, ge=max(ge, root.val) + 1)
                )
            )

        if not right_is_valid: 
            return False
        
        return True
        
if __name__ == '__main__':
    # tree = TreeNode.from_level_array([5,4,6,None,None,3,7])
    # tree = TreeNode.from_level_array([34,-6,None,-21])
    tree = TreeNode.from_level_array([3,1,5,0,2,4,6])
    print(Solution.isValidBST(tree))
