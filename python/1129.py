from collections import defaultdict, deque
from enum import Enum


class Color(Enum):
    init = 0
    red = 1
    blue = 2


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[u].append((v, Color.red))
        for u, v in blueEdges:
            graph[u].append((v, Color.blue))

        queue = deque([(0, Color.init)])
        visited = {(0, Color.init)}
        step = 0
        res = [-1] * n

        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                if res[node] == -1:
                    res[node] = step
                for next_node, next_color in graph[node]:
                    if (next_node, next_color) not in visited and next_color != color:
                        visited.add((next_node, next_color))
                        queue.append((next_node, next_color))
            step += 1

        return res
