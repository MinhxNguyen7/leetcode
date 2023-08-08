from math import prod

MIN_NUM = -pow(2, 31)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        def find_prod(left: int, right: int) -> int:
            total_prod = 1
            first_neg_index = right
            last_neg_index = left - 1
            
            if right - left <= 1:
                return nums[left]
            
            for i, num in enumerate(nums[left:right], left):
                total_prod *= num
                if num < 0:
                    first_neg_index = min(first_neg_index, i)
                    last_neg_index = max(last_neg_index, i)

            # Even number of negatives
            if total_prod > 0:
                return total_prod
            
            left_prod = prod(nums[left:first_neg_index + 1])
            right_prod = prod(nums[last_neg_index:right])
            return int(total_prod / max(left_prod, right_prod))
        
        left = 0
        max_prod = MIN_NUM
        for i, num in enumerate(nums):
            if num == 0:
                max_prod = max(max_prod, find_prod(left, i), 0)
                left = i + 1
            elif i == len(nums) - 1:
                max_prod = max(max_prod, find_prod(left, i + 1))

        return max_prod
                
if __name__ == '__main__':
    print(Solution().maxProduct([0]))