#include <unordered_map>
#include <cmath>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& points, int k) {
        // Distance of each point to origin
        std::unordered_map<unsigned, unsigned> dist;
        std::vector<unsigned> indicies{};

        for (unsigned i{}; i < points.size(); ++i) {
            dist.emplace(
                i, std::pow(points[i][0], 2) + std::pow(points[i][1], 2)
            );
            indicies.push_back(i);
        }

        const auto compare = [&](const unsigned first, const unsigned second) {
            return dist[first] > dist[second];
        };

        std::make_heap(indicies.begin(), indicies.end(), compare);

        std::vector<std::vector<int>> ret{};

        for (unsigned i{}; i < k && i < points.size(); ++i) {
            const unsigned point_idx{indicies[0]};
            ret.push_back(std::move(points[point_idx]));
            std::pop_heap(indicies.begin(), indicies.end(), compare);
            indicies.pop_back();
        }

        return ret;

    }
};