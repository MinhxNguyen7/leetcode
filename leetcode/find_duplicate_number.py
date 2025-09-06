class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        
        while True:
            if slow == fast: break
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
            
if __name__ == '__main__':
    print(Solution().findDuplicate([3, 1, 3, 4, 2]))
    print(Solution().findDuplicate([2,5,9,6,9,3,8,9,7,1]))