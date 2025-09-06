from collections import Counter
from typing import Literal

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        board_counter: Counter[str] = Counter(char for row in board for char in row)
        word_counter: Counter[str] = Counter(word)
        
        if word_counter - board_counter:
            return False
        
        row_count = len(board)
        col_count = len(board[0])

        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def dfs(row: int, col: int, word_idx: int) -> bool:

            if row >= row_count or row < 0 or col >= col_count or col < 0 or board[row][col] != word[word_idx]:
                return False

            if word_idx == len(word) - 1: return True
            
            char = board[row][col]
            board[row][col] = "" # So that it can't be repeated

            for dy, dx in directions:
                if dfs(row + dy, col + dx, word_idx + 1): return True

            board[row][col] = char

            return False
                

        for row in range(row_count):
            for col in range(col_count):
                if dfs(row, col, 0): return True
        
        return False
    
if __name__ == '__main__':
    print(Solution().exist(
        [
            ["a", "a", "a"],
            ["A", "A", "A"],
            ["a", "a", "a"]
        ],
        "aAaaaAaaA"
    ))