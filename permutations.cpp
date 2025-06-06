#include <vector>
#include <unordered_set>
#include <iostream>

class Solution {
    static void recurse(
        std::vector<int>& workingSequence,
        const std::vector<int>& nums, 
        std::unordered_set<int>& used,
        std::vector<std::vector<int>>& res
    ) {
        if (used.size() == nums.size()) {
            std::vector<int> completed = workingSequence;
            res.push_back(completed);
            return;
        }

        for (auto num : nums) {
            const bool isUsed = used.find(num) != used.end();
            if (isUsed) continue;

            workingSequence.push_back(num);
            used.insert(num);

            recurse(workingSequence, nums, used, res);

            workingSequence.pop_back();
            used.erase(num);
        }
    }

public:
    static std::vector<std::vector<int>> permute(std::vector<int>& nums) {
        std::vector<int> workingSequence{};
        std::unordered_set<int> used{};
        std::vector<std::vector<int>> res{};

        recurse(workingSequence, nums, used, res);

        return res;
    }
};

int main() {
    std::vector<int> nums{1, 2, 3};
    Solution::permute(nums);
}