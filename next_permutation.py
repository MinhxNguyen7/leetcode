class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        # Find right-most increasing sequential pair
        pair_start = len(nums) - 2
        is_greatest = False

        for pair_end in range(len(nums) - 1, -1, -1):
            pair_start = pair_end - 1
            if nums[pair_start] < nums[pair_end]:
                break
        else:
            # Array is non-increasing, so it's greatest
            nums.sort(reverse=True)
            return

        # Find the smallest number greater than than nums[pair_start] right of it
        bubbling = pair_start + 1
        for i in range(pair_start + 1, len(nums)):
            if nums[i] > nums[pair_start] and nums[i] < nums[bubbling]:
                bubbling = i

        # Bubble up target number to pair_start's position
        for i in range(bubbling, pair_start, -1):
            # i is the right-side index for swapping
            tmp = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = tmp

        # Sort the right side
        nums[pair_start + 1 :] = sorted(nums[pair_start + 1 :])
