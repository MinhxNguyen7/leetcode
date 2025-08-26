class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        best = 0
        best_dist: int | None = None

        for first_idx, first_num in enumerate(nums):
            target_rest = target - first_num

            left = first_idx + 1
            right = len(nums) - 1

            while left < right:
                second_num = nums[left]
                third_num = nums[right]

                rest = second_num + third_num
                delta = target_rest - rest
                dist = abs(delta)

                if best_dist is None or dist < best_dist:
                    best = first_num + second_num + third_num
                    best_dist = dist

                if delta < 0:  # too big
                    right -= 1
                else:  # too small
                    left += 1

        return best


if __name__ == "__main__":
    sol = Solution()

    print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Expect 2

    print(sol.threeSumClosest([10, 20, 30, 40, 50, 60, 70, 80, 90], 1))  # Expect 60

    print(
        sol.threeSumClosest([-1000, -5, -5, -5, -5, -5, -5, -1, -1, -1], -14)
    )  # Expect -15
