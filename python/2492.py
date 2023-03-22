from collections import defaultdict, deque


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        queue = deque([1])
        visited = set()
        res = float('inf')

        while queue:
            node = queue.popleft()
            for next_node, dist in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
                res = min(res, dist)

        return res
