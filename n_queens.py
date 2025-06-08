from time import perf_counter
from typing import Iterable


class Solution:
    row_t = list[bool]
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        available_cols = set(range(n))
        partial = []

        return list(Solution.recurse(n, available_cols, partial))

    @staticmethod
    def recurse(
        n: int, available_cols: set[int], partial: list[row_t]
    ) -> Iterable[list[str]]:
        if len(partial) == n:
            yield Solution.make_table_result(partial)

        for col in list(available_cols):
            partial.append([
                True if index == col else False
                for index in range(n)
            ])
            available_cols.discard(col)

            if Solution.new_queen_diagonally_valid(partial):
                yield from Solution.recurse(n, available_cols, partial)

            available_cols.add(col)
            partial.pop()
        

    @staticmethod
    def make_table_result(
        table: list[row_t]
    ) -> list[str]:
        return [
            "".join("Q" if isQueen else "." for isQueen in row)
            for row in table
        ]

    @staticmethod
    def new_queen_diagonally_valid(partial: list[row_t]):
        row = len(partial) - 1
        col = partial[-1].index(True)

        for other_row in range(len(partial) - 1):
            diff = row - other_row

            left_diag_col = col - diff
            right_diag_col = col + diff

            if (
                left_diag_col >= 0 and partial[other_row][left_diag_col]
                or
                right_diag_col < len(partial[-1]) and partial[other_row][right_diag_col]
            ):
                return False

        return True


if __name__ == "__main__":
    TRIALS_COUNT = 5
    durations: list[float] = []
    l = []
    
    for n in range(100):
        start = perf_counter()
        
        for trial in range(TRIALS_COUNT):
            solutions = Solution().solveNQueens(n)
            if solutions:
                l.append(solutions[-1])

        end = perf_counter()
        
        per_trial = (end-start) / TRIALS_COUNT
        durations.append(per_trial)
        print(f"n={n}: {round(per_trial*1000)}ms")
        
    print(l[-1])