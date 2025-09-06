class Solution:
    def jump(self, nums: list[int]) -> int:
        nums.pop()

        if not nums: return 0

        reachable = nums[0]
        if reachable >= len(nums):
            return 1
        
        jumps_required = [1 if idx <= reachable else -1 for idx in range(len(nums))]
        jumps_required[0] = 0

        for idx, num in enumerate(nums[1:], 1):
            assert reachable >= idx

            last = idx + num
            if reachable < last:
                if last >= len(nums):
                    return jumps_required[idx] + 1
                last = min(last, len(nums) - 1)
                while reachable < last:
                    jumps_required[last] = jumps_required[idx] + 1
                    last -= 1
                reachable = idx + num

        return 1
    
if __name__ == '__main__':
    print(Solution().jump([2, 3, 1]))