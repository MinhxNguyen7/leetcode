from typing import Iterable
from queue import SimpleQueue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode|None = left
        self.right: TreeNode|None = right
    
    # Adapted from 
    # https://leetcode.com/problems/recover-binary-search-tree/solutions/32539/Tree-Deserializer-and-Visualizer-for-Python/
    @staticmethod
    def from_level_array(it: Iterable[int|None]) -> 'TreeNode|None':
        """
        Returns the tree as defined by an iterable representing the
        level-order traversal of the tree (LeetCode style)
        """
        nodes = [None if val is None else TreeNode(val) for val in it]
        
        kids = nodes[::-1]
        root = kids.pop()
        
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
                
        return root
    
    def search(self: 'TreeNode', val: int) -> 'TreeNode|None':
        if self is None: return None
        if self.val == val: return self
        
        left_search = self.left.search(val) if self.left else None
        if left_search: return left_search
        
        right_search = self.right.search(val) if self.right else None
        return right_search
        
if __name__ == '__main__':
    tree = TreeNode.from_level_array(i for i in range(10))
    