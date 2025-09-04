#include <vector>
#include <array>
#include <bitset>
#include <cstdio>


class Solution {
public:
    int singleNumber(const std::vector<int>& nums) {
        constexpr unsigned NUM_BITS{sizeof(int)*8};
        std::array<unsigned, NUM_BITS> bitCounts{};

        for (auto num : nums) {
            std::bitset<NUM_BITS> bitset{static_cast<unsigned>(num)};
            for (unsigned i{}; i < NUM_BITS; ++i) {
                bitCounts[i] += bitset[i];
            }
        }

        int ret{};
        for (unsigned i{}; i < NUM_BITS; ++i) {
            ret += (bitCounts[i] % 3) << i;
        }

        return ret;
    }
};


int main() {
    printf("%d", Solution().singleNumber(std::vector<int>{2, 2, 3, 2}));
}
