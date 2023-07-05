class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        left = 0
        right = len(nums) - 1

        mid = 0

        while left <= right:
            if right - left == 1:
                return min(nums[left], nums[right])
            
            mid = (left + right) // 2

            if nums[left] < nums[mid]:
                if nums[left] < nums[right]: 
                    return nums[left]

                left = mid

            else: 
                # if nums[mid] < nums[right]:
                #     return nums[mid]
                right = mid


if __name__ == '__main__':
    print(Solution().findMin([2, 3, 1]))