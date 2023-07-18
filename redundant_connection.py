class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parents: list[int] = [i for i in range(len(edges))]

        def find_parent(node: int) -> int:
            while parents[node] != node:
                node = parents[node]
            return node

        def union(u: int, v: int) -> None:
            parents[find_parent(u)] = find_parent(v)

        last_redundant = []
        for u, v in edges: 
            u -= 1
            v -= 1

            if find_parent(u) == find_parent(v): last_redundant = (u, v)

            union(u, v)

        return [last_redundant[0] + 1, last_redundant[1] + 1]

if __name__ == '__main__':
    print(Solution().findRedundantConnection(
        [[1,3],[3,4],[1,5],[3,5],[2,3]]
    ))