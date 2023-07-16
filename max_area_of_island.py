from itertools import product

DIRECTIONS = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
)


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def explore(row: int, col: int) -> int:
            if (
                row >= num_rows or
                row < 0 or
                col >= num_cols or
                col < 0 or
                grid[row][col] != 1
            ): return 0

            grid[row][col] = 0
            return sum(explore(row + dy, col + dx) for dy, dx in DIRECTIONS) + 1

        largest = 0
        for row, col in product(range(num_rows), range(num_cols)):
            largest = max(largest, explore(row, col))

        return largest