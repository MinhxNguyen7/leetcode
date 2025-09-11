#include <vector>


class Solution {
public:
    bool canSplitArray(std::vector<int>& nums, int m) {
        if (nums.size() <= 2) {
            return true;
        }

        auto it{nums.begin()}, next{it + 1};
        for (; next < nums.end(); ++it, ++next) {
            const auto next{it + 1};
            if (*it + *next >= m) {
                return true;
            }
        }

        return false;
    }
};
