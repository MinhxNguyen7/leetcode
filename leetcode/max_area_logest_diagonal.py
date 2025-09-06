class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_diag_squared = 0
        curr_area = 0

        for h, w in dimensions:
            diag_squared = h**2 + w**2

            if diag_squared > max_diag_squared:
                max_diag_squared = diag_squared
                curr_area = h * w
            elif diag_squared == max_diag_squared:
                area = h * w
                if area > curr_area:
                    curr_area = area

        return curr_area
