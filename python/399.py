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
        for vertices, value in zip(equations, values):
            source, target = vertices
            self.graph[source].append((target, value))
            self.graph[target].append((source, 1 / value))

    def find_path(self, query):
        var1, var2 = query

        if var1 not in self.graph or var2 not in self.graph:
            return -1.0

        queue = deque([(var1, 1.0)])
        visited = set()

        while queue:
            variable, value = queue.popleft()

            if variable == var2:
                return value

            visited.add(variable)

            for next_variable, next_value in self.graph[variable]:
                if next_variable not in visited:
                    queue.append((next_variable, value * next_value))

        return -1.0
