# https://leetcode.com/problems/find-eventual-safe-states/solutions/816985/python-easy-solution-graph-coloring-98-69/

VISITING = 1
VISITED = 2


class Solution:

    def __init__(self):
        self.graph = []
        self.visited = []

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        self.graph = graph
        self.visited = [0] * len(graph)

        for node in range(len(graph)):
            self.cycle(node)

        return [i for i in range(len(graph)) if self.visited[i] == VISITED]

    def cycle(self, node):
        if self.visited[node] == VISITING:
            return True
        if self.visited[node] == VISITED:
            return False

        self.visited[node] = VISITING

        for next_node in self.graph[node]:
            if self.cycle(next_node):
                return True

        self.visited[node] = VISITED
        return False
