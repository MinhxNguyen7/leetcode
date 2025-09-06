class Solution:
    def subsets(self, nums: list[int], res: list[list[int]]|None = None) -> list[list[int]]:
        if res is None: res = [[]]
        
        for num in nums:
            initial_length = len(res)
            for i in range(initial_length):
                res.append(res[i] + [num])
        
        return res
    
if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))