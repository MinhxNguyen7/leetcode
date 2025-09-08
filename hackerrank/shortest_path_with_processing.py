from collections import defaultdict
from heapq import heappop, heappush


def computeShortestDeliveryTimes(
    n: int, handlingTimes: list[int], m: int, routes: list[list[int]], source: int
):
    # Maps source to (destination, weight)
    out_edges: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

    for src, dst, w in routes:
        out_edges[src].append((dst, w))

    visited: set[int] = set()
    delays: list[int] = [-1] * n

    # Priority queue of (total_delay, node)
    heap: list[tuple[int, int]] = [(0, source)]

    while heap:
        curr_delay, curr_node = heappop(heap)

        if curr_node in visited:
            continue

        visited.add(curr_node)
        delays[curr_node] = curr_delay

        for dst, w in out_edges[curr_node]:
            if dst not in visited:
                # If we're at the source, no handling time has been incurred yet
                if curr_node == source:
                    total_delay = curr_delay + w
                else:
                    # Add handling time when leaving an intermediate node
                    total_delay = curr_delay + w + handlingTimes[curr_node]
                heappush(heap, (total_delay, dst))

    return delays


if __name__ == "__main__":
    print(
        computeShortestDeliveryTimes(
            3, [1, 2, 3], 3, [[0, 1, 4], [1, 2, 5], [0, 2, 10]], 0
        )
    )
