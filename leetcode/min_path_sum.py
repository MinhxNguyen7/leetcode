class Solution:
    @staticmethod
    def minPathSum(grid: list[list[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        sums: list[list[int]] = [
            [0] * width
        ] * height
        
        for i, grid_row in enumerate(grid):
            for j, grid_cell in enumerate(grid_row):
                if i == j == 0:
                    sums[i][j] = 0 + grid_cell
                elif i == 0:
                    sums[i][j] = sums[i][j - 1] + grid_cell
                elif j == 0: 
                    sums[i][j] = sums[i - 1][j] + grid_cell
                else:
                    sums[i][j] = min(
                        sums[i - 1][j],
                        sums[i][j - 1]
                    ) + grid_cell

        return sums[-1][-1]

if __name__ == '__main__':
    print(Solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]])) # 7
    print(Solution.minPathSum([[1,2,3],[4,5,6]])) # 12