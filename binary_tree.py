from typing import Iterable
from queue import SimpleQueue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # From https://leetcode.com/problems/recover-binary-search-tree/solutions/32539/Tree-Deserializer-and-Visualizer-for-Python/
    @staticmethod
    def from_level_array(string: str) -> 'TreeNode|None':
        """
        Returns the tree as defined by a string representing the
        level-order traversal of the tree (LeetCode style)
        """
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val))
                for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
        return root

if __name__ == '__main__':
    string = "[" + ",".join(str(i) for i in range(10)) + "]"
    print(string)
    tree = TreeNode.from_level_array(string)