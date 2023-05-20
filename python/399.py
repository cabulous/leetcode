from collections import defaultdict, deque


# https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = self.build_graph(equations, values)
        return [self.find_path(graph, q) for q in queries]

    def build_graph(self, equations, values):
        graph = defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))
        return graph

    def find_path(self, graph, query):
        source, target = query
        if source not in graph or target not in graph:
            return -1.0

        queue = deque([(source, 1.0)])
        visited = {source}

        while queue:
            node, val = queue.popleft()
            if node == target:
                return val
            for next_node, next_val in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node, val * next_val))

        return -1.0
