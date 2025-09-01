#include <vector>
#include <algorithm>

class Solution {
public:
    void rotate(std::vector<std::vector<int>>& matrix) {
        // Mirror top to bottom by swapping the rows
        std::reverse(matrix.begin(), matrix.end());

        const auto N{matrix.size()};

        // Transpose the matrix
        for (unsigned i{}; i < N; ++i) {
            for (unsigned j{i + 1}; j < N; ++j) {
                std::swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};
