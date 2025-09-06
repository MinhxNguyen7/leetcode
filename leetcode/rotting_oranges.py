from collections import deque
from itertools import product

DIRECTIONS = (
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
)

# See also
# https://leetcode.com/problems/rotting-oranges/solutions/388104/python-10-lines-bfs-beat-97/

class Solution:
    @staticmethod
    def orangesRotting(grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Append all rotten oranges to queue
        queue: deque[tuple[int, int]] = deque()
        
        num_fresh = 0
        for row, col in product(range(num_rows), range(num_cols)):
            if grid[row][col] == 2:
                queue.append((row, col))
                # Represents negative minutes required to get to this orange
                grid[row][col] = 0
            
            # Increment num_fresh if there's a fresh orange in this cell
            num_fresh += (grid[row][col] == 1)

        # BFS
        time_required = 0
        while len(queue) and num_fresh > 0:
            row, col = queue.popleft()
            next_dist = grid[row][col] - 1
            
            for dy, dx in DIRECTIONS:
                next_row, next_col = row + dy, col + dx
                if (
                    # If out of bounds
                    next_row >= num_rows or
                    next_row < 0 or
                    next_col >= num_cols or
                    next_col < 0 or
                    # If empty or already rotten
                    grid[next_row][next_col] != 1
                ): continue
                
                num_fresh -= 1
                time_required = min(next_dist, time_required)
                grid[next_row][next_col] = next_dist
                queue.append((next_row, next_col))

        return -time_required if num_fresh == 0 else -1
    
if __name__ == '__main__':
    print(Solution().orangesRotting([
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]))