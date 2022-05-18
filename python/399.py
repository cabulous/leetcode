from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion
class Solution:

    def __init__(self):
        self.graph = defaultdict(list)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.build_graph(equations, values)
        return [self.find_path(q) for q in queries]

    def build_graph(self, equations, values):
        for [source, target], value in zip(equations, values):
            self.graph[source].append((target, value))
            self.graph[target].append((source, 1 / value))

    def find_path(self, query):
        source, target = query

        if source not in self.graph or target not in self.graph:
            return -1.0

        queue = deque([(source, 1.0)])
        visited = {source}

        while queue:
            node, value = queue.popleft()

            if node == target:
                return value

            for next_node, next_value in self.graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node, value * next_value))

        return -1.0
