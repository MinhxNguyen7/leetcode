class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_size = len(matrix[0])

        left = 0
        right = row_size * len(matrix)

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, row_size)
            
            if row >= len(matrix): return False
            
            val = matrix[row][col]

            if val == target:
                return True

            if val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
    
if __name__ == "__main__":
    print(Solution().searchMatrix([[1]], 2))