#include <algorithm>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::make_heap(nums.begin(), nums.end());

        auto endIt{nums.end()};

        for (unsigned i{1}; i < k; ++i) {
            std::pop_heap(nums.begin(), endIt);
            --endIt;
        }

        return nums[0];

    }
};