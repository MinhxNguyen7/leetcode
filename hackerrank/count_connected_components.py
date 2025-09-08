def dfs(root: int, adjacencies: list[list[int]], seen: list[bool]):
    if seen[root]:
        return

    seen[root] = True

    for child in adjacencies[root]:
        dfs(child, adjacencies, seen)


def countIsolatedCommunicationGroups(links: list[list[int]], n: int):
    adjacencies: list[list[int]] = [list() for _ in range(n)]
    for a, b in links:
        adjacencies[a].append(b)
        adjacencies[b].append(a)

    seen: list[bool] = [False] * n
    components = 0

    for i in range(n):
        if seen[i]:
            continue

        components += 1
        dfs(i, adjacencies, seen)

    return components


if __name__ == "__main__":
    print(countIsolatedCommunicationGroups([], 10))  # 10
