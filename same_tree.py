from binary_tree import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode|None, q: TreeNode|None) -> bool:
        if p == q == None: return True

        if p is None or q is None: return False # Only one is None

        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
