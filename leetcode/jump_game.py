class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reachable = nums[0]
        for idx, num in enumerate(nums[1:], 1):
            if reachable >= len(nums) - 1: return True
            if reachable < idx: return False
            reachable = max(reachable, idx + num)
        
        return True
    
if __name__ == '__main__':
    print(Solution().canJump([3,0,8,2,0,0,1]))