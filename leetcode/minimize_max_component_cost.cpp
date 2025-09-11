#include <vector>
#include <algorithm>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <iostream>

class Solution
{
    typedef int node_t, weight_t;
    typedef std::vector<std::vector<std::pair<node_t, weight_t>>> graph_t;

    struct Edge
    {
        node_t first;
        node_t second;

        bool operator==(const Edge &other) const
        {
            return first == other.first && second == other.second;
        }
    };

    struct EdgeAndWeight
    {
        Edge edge;
        weight_t weight;
    };

    struct EdgeHash
    {
        size_t operator()(const Edge &key) const
        {
            static const auto hasher{std::hash<node_t>()};
            return (
                hasher(key.first) ^ ((hasher(key.second) << 1) >> 1));
        }
    };

    class EdgeGreater
    {
    public:
        bool operator()(const EdgeAndWeight &a, const EdgeAndWeight &b)
        {
            return a.weight > b.weight;
        }
    };

    static graph_t makeGraph(
        unsigned n, const std::vector<std::vector<int>> &edges)
    {
        graph_t graph{};
        for (size_t i{}; i < n; ++i)
        {
            graph.push_back(std::vector<std::pair<node_t, weight_t>>{});
        }

        for (const auto &edge : edges)
        {
            const node_t first{edge[0]}, second{edge[1]};
            const weight_t weight{edge[2]};

            graph[first].push_back({second, weight});
            graph[second].push_back({first, weight});
        }

        return graph;
    }

    static std::unordered_set<Edge, EdgeHash> computeMST(const graph_t &graph)
    {
        std::unordered_set<Edge, EdgeHash> mst{};

        std::priority_queue<
            EdgeAndWeight,
            std::vector<EdgeAndWeight>,
            EdgeGreater>
            queue{};

        std::unordered_set<node_t> visited{};

        // Start from node 0
        if (graph.empty() || graph[0].empty())
        {
            return mst;
        }

        visited.insert(0);

        // Add all edges from node 0
        for (const auto &[neighbor, weight] : graph[0])
        {
            queue.push(EdgeAndWeight{{0, neighbor}, weight});
        }

        while (!queue.empty())
        {
            const auto [edge, weight] = queue.top();
            const auto [from, to] = edge;
            queue.pop();

            // Skip edge if next node already visited
            if (visited.find(to) != visited.end())
            {
                continue;
            }

            // This is the min-edge that crosses the cut
            mst.insert({from, to});

            // Add newly discovered nodes to queue
            for (const auto &[toNext, nextWeight] : graph[to])
            {
                if (visited.find(toNext) == visited.end())
                {
                    queue.push(EdgeAndWeight{{to, toNext}, nextWeight});
                }
            }

            visited.insert(to);
        }

        return mst;
    }

public:
    static int minCost(int n, std::vector<std::vector<int>> edges, int k)
    {
        if (edges.size() < static_cast<unsigned>(k))
        {
            return 0;
        }

        const auto graph{makeGraph(n, edges)};
        const auto mst{computeMST(graph)};

        if (mst.size() < static_cast<unsigned>(k))
        {
            return 0;
        }

        std::sort(
            edges.begin(), edges.end(),
            [](const auto &a, const auto &b)
            {
                return a[2] > b[2];
            });

        int numComponents{};
        weight_t maxCost{};

        for (auto it{edges.begin()}; it != edges.end() && numComponents < k; ++it)
        {
            const node_t first{(*it)[0]}, second{(*it)[1]};
            const weight_t weight{(*it)[2]};

            const bool edgeInMst{
                mst.find({first, second}) != mst.end() || mst.find({second, first}) != mst.end()};
            if (edgeInMst)
            {
                numComponents += 1;
                maxCost = weight;
            }
        }

        return maxCost;
    }
};

int main()
{
    std::cout << Solution::minCost(5, {{0, 1, 4}, {1, 2, 3}, {1, 3, 2}, {3, 4, 6}}, 2) << '\n'; // 4
    std::cout << Solution::minCost(4, {{0, 1, 5}, {1, 2, 5}, {2, 3, 5}}, 4) << '\n';            // 0
    std::cout << Solution::minCost(4, {{0, 1, 82}, {0, 2, 83}, {1, 2, 54}}, 4) << '\n';         // 0
}