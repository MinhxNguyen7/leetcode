#include <map>
#include <vector>
#include <cassert>
#include <iostream>

#include "cpp_utils/printing.h"

// NOTE: This is is O(nlogn), whereas the optimal solution is O(n)
class Solution
{
public:
    static std::vector<int> mostCompetitive(const std::vector<int> &nums, int k)
    {
        unsigned kCast{static_cast<unsigned>(k)};

        if (nums.size() < 2 || nums.size() < kCast)
        {
            return nums;
        }

        std::vector<int> ret(kCast);

        std::map<const int, unsigned> counts{};

        // Start and (after) end of window
        auto left{nums.begin()}, right{nums.begin()};
        auto end{nums.end()};

        for (unsigned i{}; kCast; ++i, --kCast)
        {
            for (; end - right >= kCast; ++right)
            {
                auto rightNum{*right};
                if (!counts.contains(rightNum))
                {
                    counts.insert({rightNum, 0});
                }
                ++counts[rightNum];
            }

            const auto [num, count] = *counts.begin();

            // Shrink window from left until we find `num`
            for (; *left != num; ++left)
            {
                const auto leftNum{*left};

                --counts[leftNum];
                if (counts[leftNum] == 0)
                {
                    counts.erase(leftNum);
                }
            }

            assert(*left == num);

            // Shrink the window *past* num
            --counts[num];
            if (counts[num] == 0)
            {
                counts.erase(num);
            }
            ++left;

            ret[i] = num;
        }

        return ret;
    }
};

int main()
{
    // [2, 6]
    const auto res = Solution::mostCompetitive({3, 5, 2, 6}, 2);
    printIt(res.begin(), res.end());

    // [2, 3, 3, 4]
    const auto res = Solution::mostCompetitive({2, 4, 3, 3, 5, 4, 9, 6}, 4);
    printIt(res.begin(), res.end());
}