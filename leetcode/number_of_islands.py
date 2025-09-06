from itertools import product

DIRECTIONS = (
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
)

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def mark_island(row: int, col: int) -> None:
            if (
                row >= num_rows or
                row < 0 or
                col >= num_cols or
                col < 0 or
                grid[row][col] == "0"
            ): return

            grid[row][col] = "0"

            for dy, dx in DIRECTIONS:
                mark_island(row + dy, col + dx)

        count = 0
        for row, col in product(range(num_rows), range(num_cols)):
            if grid[row][col] == "1":
                count += 1
                mark_island(row, col)
        
        return count