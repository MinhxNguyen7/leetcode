DIRECTIONS = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
)

class Solution:
    @staticmethod
    def pacificAtlantic(heights: list[list[int]]):
        num_rows = len(heights)
        num_cols = len(heights[0])
        
        def ocean_dfs(row: int, col: int, ocean_set: set[tuple[int, int]]) -> None:
            """
            Assumes that the cell (row, col) drains to the same ocean as parent
            and recursively adds adjacent cells with heigher/same height
            """
            ocean_set.add((row, col))
            
            for dy, dx in DIRECTIONS:
                next_row, next_col = row + dy, col + dx

                if (
                    next_row >= num_rows or
                    next_row < 0 or
                    next_col >= num_cols or
                    next_col < 0 or
                    (next_row, next_col) in ocean_set or
                    heights[next_row][next_col] < heights[row][col]
                ): continue

                ocean_dfs(next_row, next_col, ocean_set)

        to_pacific: set[tuple[int, int]] = set()
        to_atlantic: set[tuple[int, int]] = set()
        
        for row in range(num_rows):
            ocean_dfs(row, 0, to_pacific)
            ocean_dfs(row, num_cols - 1, to_atlantic)

        for col in range(num_cols):
            ocean_dfs(0, col, to_pacific)
            ocean_dfs(num_rows - 1, col, to_atlantic)

        return to_pacific & to_atlantic

if __name__ == '__main__':
    print(Solution().pacificAtlantic([
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]))