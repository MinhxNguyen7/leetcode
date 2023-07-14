class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        solutions: list[list[int]] = []
        candidates.sort()

        def dfs(offset: int, path: list[int], target: int) -> None:
            if target == 0:
                solutions.append(path.copy())
                return
            
            if target < 0 or offset >= len(candidates): 
                return
            
            path.append(candidates[offset])
            dfs(offset + 1, path, target-path[-1])
            path.pop()
            
            forward = offset + 1
            if forward >= len(candidates): return
            while candidates[forward] == candidates[offset]:
                forward += 1
                if forward >= len(candidates): return


            dfs(forward, path, target)

        dfs(0, [], target)
        return solutions
    
if __name__ == '__main__':
    print(Solution().combinationSum2([5], 5))
    