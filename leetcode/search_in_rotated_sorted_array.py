class Solution:
    def search(self, nums: list[int], target: int) -> int:

        def binary_search(l: int, r: int):
            """
            Performs a normal binary search on the sorted slice defined by nums[l:r+1]
            """
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target: return m
                
                if nums[m] < target: l = m + 1
                else: r = m - 1
            
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Right side (inclusive) is naturally ordered
            right_is_natural = nums[mid] <= nums[right]
            # left side (inclusive) is naturally ordered
            left_is_natural = nums[left] <= nums[mid]

            # Note: At least one side is necessarily naturally ordered

            if right_is_natural and left_is_natural:
                return binary_search(left, right)

            if target < nums[mid]:
                if right_is_natural or nums[left] <= target:
                    right = mid - 1
                else: 
                    left = mid + 1
                
            else:
                if left_is_natural or nums[right] >= target:
                    left = mid + 1
                else: 
                    right = mid - 1

        return -1

if __name__ == '__main__':
    print(Solution().search([3, 5, 1], 3))