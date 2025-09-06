class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ret: list[list[int]] = []
        def dfs(target: int, stack: list[int], start_from: int) -> None:
            if target == 0:
                ret.append(stack.copy())

            if target < 2:
                return
            
            for offset, num in enumerate(candidates[start_from:]):
                stack.append(num)
                dfs(target - num, stack, start_from + offset)
                stack.pop()
        
        dfs(target, [], 0)

        return ret

if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))