class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ret: list[list[int]] = [[]]

        nums.sort()
        stack = []
        def dfs(offset: int):
            for idx in range(offset, len(nums)):
                num = nums[idx]
                if idx > offset and num == nums[idx - 1]: continue
                stack.append(num)
                ret.append(stack.copy())
                dfs(idx + 1)
                stack.pop()

        dfs(0)
        
        return ret
    
if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))