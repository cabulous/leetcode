from collections import defaultdict


# https://leetcode.com/problems/number-of-operations-to-make-network-connected/solutions/477679/python-count-the-connected-networks/?orderBy=most_votes
class Solution:

    def __init__(self):
        self.graph = defaultdict(set)
        self.seen = []

    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        for u, v in connections:
            self.graph[u].add(v)
            self.graph[v].add(u)

        self.seen = [False] * n

        return sum(self.count_group(i) for i in range(n)) - 1

    def count_group(self, node):
        if self.seen[node]:
            return 0

        self.seen[node] = True

        for next_node in self.graph[node]:
            self.count_group(next_node)

        return 1
