from binary_tree import TreeNode
from collections import deque
from typing import Iterable

class Solution:
    def levelOrder(self, root: TreeNode|None) -> Iterable[Iterable[int]]:
        queue: deque[TreeNode|None] = deque()
        queue.append(root)
        queue.append(None)

        while queue[0] is not None:
            row = []

            while True:
                node = queue.popleft()
                if node is None: 
                    queue.append(None)
                    break
                
                row.append(node.val)
                if node.left is not None: queue.append(node.left)
                if node.right is not None: queue.append(node.right)
            
            yield row
