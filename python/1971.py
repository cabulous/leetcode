from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        seen = {source}

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for next_node in graph[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    queue.append(next_node)

        return False
