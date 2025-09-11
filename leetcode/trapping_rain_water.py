class Solution:
    def trap(self, heights: list[int]) -> int:
        if len(heights) < 3:
            return 0

        heights.append(0)

        water = 0
        i = 0
        while i + 1 < len(heights):
            i_height = heights[i]
            # Find one that's higher, or the highest subsequently available otherwise.
            next_big = i + 1
            for j in range(i + 1, len(heights)):
                j_height = heights[j]
                if j_height > heights[next_big]:
                    next_big = j

                if j_height > i_height:
                    break

            pool_height = min(i_height, heights[next_big])
            for between in range(i + 1, next_big):
                water += pool_height - heights[between]

            i = next_big

        return water


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
