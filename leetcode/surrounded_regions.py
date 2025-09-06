from itertools import product

DIRECTIONS = (
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
)

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_rows = len(board)
        num_cols = len(board[0])

        def mark(row: int, col: int) -> None:
            if (
                row >= num_rows or
                row < 0 or
                col >= num_cols or
                col < 0 or
                board[row][col] == "X" or
                board[row][col] == ""
            ): return

            board[row][col] = ""

            for dy, dx in DIRECTIONS:
                mark(row + dy, col + dx)

        for row in range(num_rows):
            mark(row, 0)
            mark(row, num_cols - 1)
        
        for col in range(num_cols):
            mark(0, col)
            mark(num_rows - 1, col)

        for row, col in product(range(num_rows), range(num_cols)):
            if board[row][col] == "O": board[row][col] = "X"
            if board[row][col] == "": board[row][col] = "O"

if __name__ == '__main__':
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    Solution().solve(board)
    print(board)