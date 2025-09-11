#include <vector>
#include <iostream>

class Solution
{
public:
    static int trap(const std::vector<int> &heights)
    {
        std::vector<int> leftMax(heights.size()), rightMax(heights.size());

        int runningMax{};
        for (size_t i{}; i < leftMax.size(); ++i)
        {
            runningMax = std::max(runningMax, heights[i]);
            leftMax[i] = runningMax;
        }

        runningMax = 0;
        for (size_t i{rightMax.size() - 1}; i != 0; --i)
        {
            runningMax = std::max(runningMax, heights[i]);
            rightMax[i] = runningMax;
        }

        int water{};
        for (size_t i{}; i < heights.size(); ++i)
        {
            water += std::max(0, std::min(leftMax[i], rightMax[i]) - heights[i]);
        }

        return water;
    }
};

int main()
{
    // 6
    std::cout << Solution::trap({0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}) << '\n';

    // 9
    std::cout << Solution::trap({4, 2, 0, 3, 2, 5}) << '\n';
}