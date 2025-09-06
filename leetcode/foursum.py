class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []

        nums.sort()

        for first_idx, first in enumerate(nums):
            # Skip repeating
            if first_idx != 0 and first == nums[first_idx - 1]:
                continue

            for fourth_idx in range(len(nums) - 1, first_idx + 2, -1):
                fourth = nums[fourth_idx]

                # Skip repeating
                if fourth_idx + 1 < len(nums) and fourth == nums[fourth_idx + 1]:
                    continue

                second_idx = first_idx + 1
                third_idx = fourth_idx - 1
                while second_idx < third_idx:
                    second = nums[second_idx]
                    third = nums[third_idx]

                    delta = target - (first + second + third + fourth)
                    if delta > 0:
                        second_idx += 1
                    elif delta < 0:
                        third_idx -= 1
                    else:
                        res.append([first, second, third, fourth])

                        second_idx += 1
                        while (
                            nums[second_idx] == nums[second_idx - 1]
                            and second_idx < fourth_idx
                        ):
                            second_idx += 1

                        third_idx -= 1
                        while (
                            nums[third_idx] == nums[third_idx + 1]
                            and third_idx > first_idx
                        ):
                            third_idx -= 1

        return res


if __name__ == "__main__":
    print(
        Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    )  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    print(Solution().fourSum([2, 2, 2, 2, 2], 8))  # [[2, 2, 2, 2]]

    print(Solution().fourSum([-3, -1, 0, 2, 4, 5], 0))  # [[-3,-1,0,4]]
