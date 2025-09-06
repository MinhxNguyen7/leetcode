class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0: return int(bool(poured))

        curr_row = [poured]
        for _ in range(1, query_row + 1):
            empty_row = True
            next_row = [0.0 for _ in range(len(curr_row) + 1)]
            for index, glass in enumerate(curr_row):
                if not glass: continue
                
                empty_row = False
                half = max(glass - 1, 0) / 2
                next_row[index] += half
                next_row[index+1] += half
            if empty_row: return 0
            curr_row = next_row

        return min(curr_row[query_glass], 1)
    
if __name__ == '__main__':
    # a = [0.0 for _ in range(pow(2, 99))]
    print(Solution().champagneTower(2, 1, 1))