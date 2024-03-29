#include <array>
#include <stack>
#include <vector>
#include <iostream>

typedef std::pair<char, char> LocationT;
typedef std::vector<std::vector<char>> BoardT;

class Solution {
    std::array<std::array<std::array<bool, 9>, 3>, 3> squares;
    std::array<std::array<bool, 9>, 9> rows;
    std::array<std::array<bool, 9>, 9> cols;

    std::vector<LocationT> toDo;
    char next = 0;

    static inline char charToInt(char c) {
        return c - 48;
    }

    inline void fillCountersFalse() {
        for (auto& row : rows) {
            std::fill(row.begin(), row.end(), false);
        }

        for (auto& col : cols) {
            std::fill(col.begin(), col.end(), false);
        }

        for (auto& squareRow : squares) {
            for (auto & square : squareRow) {
                std::fill(square.begin(), square.end(), false);
            }
        }
    }

    void populateCounters(const BoardT& board) {
        for (char row = 0; row < board.size(); ++row) {
            for (char col = 0; col < board[row].size(); ++ col) {
                const char cell = board[row][col];

                if (cell == '.') {
                    toDo.push_back(std::make_pair(row, col));
                    continue;
                }

                const char number = charToInt(cell);
                setCounter(std::make_pair(row, col), number, true);
            }
        }
    }

    /**
     * Checks whether a number at a prospective location would be valid
    */
    inline bool checkValid(LocationT location, char number) {
        const char row = location.first;
        const char col = location.second;

        return !(
            rows[row][number] ||
            cols[col][number] || 
            squares[row/3][col/3][number]
        );
    }

    void setCounter(LocationT location, char number, bool value) {
        const char row = location.first;
        const char col = location.second;

        squares[row / 3][col / 3][number] = value;
        rows[row][number] = value;
        cols[col][number] = value;
    }

    bool dfs(BoardT& board) {
        if (next == toDo.size()) return true; // Done

        const LocationT location =  toDo[next];
        const char row = location.first;
        const char col = location.second;
        char& cell = board[row][col];
        next += 1;

        for (char digit = '1'; digit <= '9' ; ++digit) {
            const auto number = charToInt(digit);

            if (!checkValid(location, number)) continue;

            cell = digit;
            setCounter(location, number, true);

            if (dfs(board)) return true;
            
            cell = '.';
            setCounter(location, number, false);
        }

        next -= 1;
        return false;
    }

public:
    Solution(): toDo{}, next{0} {
        fillCountersFalse();
    }

    void solveSudoku(BoardT& board) {
        populateCounters(board);
        bool res = dfs(board);
    }
};

// void printSudoku(const BoardT& board) {
//     std::cout << "-------------------------\n";
//     for (auto& row : board) {
//         for (const char cell : row) {
//             std::cout << cell << ' ';
//         }
//         std::cout << '\n';
//     }
//     std::cout << "-------------------------\n";
// } 

// int main() {
//     BoardT board = {
//         {'5','3','.','.','7','.','.','.','.'},
//         {'6','.','.','1','9','5','.','.','.'},
//         {'.','9','8','.','.','.','.','6','.'},
//         {'8','.','.','.','6','.','.','.','3'},
//         {'4','.','.','8','.','3','.','.','1'},
//         {'7','.','.','.','2','.','.','.','6'},
//         {'.','6','.','.','.','.','2','8','.'},
//         {'.','.','.','4','1','9','.','.','5'},
//         {'.','.','.','.','8','.','.','7','9'}
//     };

//     printSudoku(board);

//     Solution().solveSudoku(board);

//     printSudoku(board);
// }