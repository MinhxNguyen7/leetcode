#include <utility>
#include <vector>
#include <algorithm>
#include <array>

#include <limits.h>
#include <stdlib.h> 
#include <iostream>

class Solution {
public:
    int minimumDeletions(const std::vector<int>& nums) {
        if (nums.empty()) return 0;

        int minStart{INT_MAX}, maxStart{INT_MIN}, minEnd{INT_MAX}, maxEnd{INT_MIN};
        size_t minStartIdx{}, maxStartIdx{}, minEndIdx{}, maxEndIdx{};

        for (size_t i{}; i < nums.size(); ++i) {
            const auto num{nums[i]};

            if (num > maxStart) {
                maxStart = num;
                maxStartIdx = i;
            }

            if (num < minStart) {
                minStart = num;
                minStartIdx = i;
            }

            if (num >= maxEnd) {
                maxEnd = num;
                maxEndIdx = i;
            }

            if (num <= minEnd) {
                minEnd = num;
                minEndIdx = i;
            }
        }

        // If min and max are the same, the whole sequence is the same
        if (minStart == maxStart) return 1;

        // Number of deletions required for each of the four deletion options
        const unsigned startStart = std::max(minStartIdx, maxStartIdx) + 1;
        const unsigned endEnd = nums.size() - std::min(minEndIdx, maxEndIdx);
        const unsigned startEnd = minStartIdx + 1 +(nums.size() - maxEndIdx);
        const unsigned endStart = maxStartIdx + 1 + (nums.size() - minEndIdx);

        const std::array deletions{startStart, endEnd, startEnd, endStart};

        return *std::min_element(deletions.begin(), deletions.end());
    }
};

int main() {
    Solution sol{};

    // 5
    std::cout << sol.minimumDeletions({2,10,7,5,4,1,8,6}) << '\n';

    // 3
    std::cout << sol.minimumDeletions({0,-4,19,1,8,-2,-3,5}) << '\n';
}
