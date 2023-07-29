from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        edges: defaultdict[int, dict[int, int]] = defaultdict(dict)

        for origin, destination, price in flights:
            edges[origin][destination] = price

        # (price, destination, # of stops)
        heap: list[tuple[int, int, int]] = [(0, src, 0)]

        # distaces[destination][stops] = price
        distances: defaultdict[int, dict[int, int]] = defaultdict(dict)
        distances[src][0] = 0

        while heap:
            current_dist, current, stops = heappop(heap)

            if current == dst: return current_dist

            if stops > k:
                continue
                
            for node, dist in edges[current].items():
                new_dist = current_dist + dist

                if (
                    stops + 1 not in distances[node] or
                    distances[node][stops + 1] > new_dist
                ):
                    heappush(heap, (new_dist, node, stops + 1))
                    distances[node][stops + 1] = new_dist
        
        return -1