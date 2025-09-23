from collections import defaultdict


class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Mapping of number to position in the array nums2
        nums2_positions: defaultdict[int, list[int]] = defaultdict(list)
        for index, num2 in enumerate(nums2):
            nums2_positions[num2].append(index)

        nums1.sort()
        nums2.sort()

        result: list[int] = []

        pointer = 0  # To look through nums1
        unused: list[int] = []
        for num2 in nums2:
            # Advance pointer until there's a number in nums1 that's greater
            while pointer < len(nums1) and nums1[pointer] <= num2:
                unused.append(nums1[pointer])
                pointer += 1

            if pointer >= len(nums1):
                break

            result.append(nums1[pointer])
            pointer += 1

        result.extend(unused)

        assert len(result) == len(nums1)

        # Rearrage to original order
        reordered: list[int] = [0] * len(result)
        for num1, num2 in zip(result, nums2):
            index = nums2_positions[num2].pop()
            reordered[index] = num1

        return reordered


if __name__ == "__main__":
    sol = Solution()

    print(sol.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))  # [2,11,7,15]
    print(sol.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))  # [24,32,8,12]
