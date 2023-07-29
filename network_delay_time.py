from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges: defaultdict[int, dict[int, int]] = defaultdict(dict)

        for origin, destination, time in times:
            edges[origin][destination] = time

        heap: list[tuple[int, int]] = [(0, k)]
        distances: dict[int, int] = {k: 0}

        while heap:
            time, current = heappop(heap)
            
            for node, distance in edges[current].items():
                new_distance = distances[current] + distance
                if (
                    node not in distances or
                    new_distance < distances[node]
                ):
                    distances[node] = new_distance
                    heappush(heap, (new_distance, node))

        if not all(i in distances for i in range(1, n + 1)):
            # Not connected
            return -1

        return max(distances.values())
    
if __name__ == '__main__':
    print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))