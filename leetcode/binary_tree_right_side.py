from binary_tree import TreeNode

class Solution:
    @staticmethod
    def rightSideView(root: TreeNode|None, ret: list[int]|None = None, depth: int = 0) -> list[int]:
        if not root: return []

        if ret is None: ret = []

        if len(ret) <= depth:
            ret.append(root.val)

        Solution.rightSideView(root.right, ret, depth + 1)
        Solution.rightSideView(root.left, ret, depth + 1)

        return ret 