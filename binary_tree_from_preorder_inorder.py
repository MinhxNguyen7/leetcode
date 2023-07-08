from binary_tree import TreeNode
from collections import deque

class Solution:
    @staticmethod
    def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode|None:
        pre_queue = deque(preorder)

        in_map: dict[int, int] = {}
        for index, val in enumerate(inorder):
            in_map[val] = index

        def build(left: int, right: int) -> TreeNode|None:
            if left == right: return None

            root_val = pre_queue.popleft()

            if left + 1 == right: return TreeNode(root_val)
            
            return TreeNode(
                root_val, 
                build(left, in_map[root_val]),
                build(in_map[root_val] + 1, right)
            )

        return build(0, len(pre_queue))
    
if __name__ == '__main__':
    # Solution.buildTree([3,9,20,15,7], inorder = [9,3,15,20,7])
    Solution.buildTree([1, 2, 3], inorder = [3, 2, 1])
    