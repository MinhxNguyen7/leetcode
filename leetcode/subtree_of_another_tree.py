from binary_tree import TreeNode

class Solution:
    @staticmethod
    def isSameTree(p: TreeNode|None, q: TreeNode|None) -> bool:
        if p == q == None: return True

        if p is None or q is None: return False # Only one is None

        if p.val != q.val: return False

        return Solution.isSameTree(p.left, q.left) and Solution.isSameTree(p.right, q.right)

    def isSubtree(self, root: TreeNode|None, subRoot: TreeNode|None) -> bool:
        # If they're both None, they would be evaluated as equal in Solution.isSameRoot,
        # and the boolean expression would short-circuit and not evaluate sub-trees,
        # so we only need to check if one is None here.
        if root is None or subRoot is None: return False

        return (
            Solution.isSameTree(root, subRoot) or 
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )