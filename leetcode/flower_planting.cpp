#include <vector>
#include <array>

#include "cpp_utils/printing.h"

class Solution {
public:
    static std::vector<int> gardenNoAdj(
        int n, const std::vector<std::vector<int>>& paths
    ) {
        std::vector<std::vector<int>> adjacencies(n);

        for (auto& path : paths) {
            const int x{path[0]}, y{path[1]};
            adjacencies[x - 1].push_back(y);
            adjacencies[y - 1].push_back(x);
        }

        std::vector<int> colors(n);
        std::fill(colors.begin(), colors.end(), 0);

        for (int garden{1}; garden <= n; ++garden) {
            // Mark the colors that have been used by adjacent gardnens
            std::array<bool, 4> used{};
            const int index{garden - 1};
            for (const auto adjacent : adjacencies[index]) {
                const auto color{colors[adjacent - 1]};
                if (color) {
                    used[color - 1] = true;
                }
            }

            // Find the first color that hasn't been used and assign it.
            for (int color{1}; color <= 4; ++color) {
                if (!used[color - 1]) {
                    colors[index] = color;
                    break;
                }
            }
        }

        return colors;
    }
};


int main() {
    const std::vector<std::vector<int>> paths {{1,2},{2,3},{3,1}};
    const auto sol = Solution::gardenNoAdj(3, paths);
    printIt(sol.begin(), sol.end());
    std::cout << '\n';
}
