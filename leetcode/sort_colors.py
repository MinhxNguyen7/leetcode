class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1

        for i in range(counts[0]):
            nums[i] = 0

        for i in range(counts[0], counts[0] + counts[1]):
            nums[i] = 1

        for i in range(counts[0] + counts[1], counts[0] + counts[1] + counts[2]):
            nums[i] = 2
