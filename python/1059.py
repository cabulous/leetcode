from typing import List
from collections import defaultdict


# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/discuss/304940/Python-straightforward-DFS
class Solution:

    def __init__(self):
        self.graph = defaultdict(list)
        self.seen = set()
        self.destination = 0

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        for u, v in edges:
            self.graph[u].append(v)

        self.destination = destination

        return self.reachable(source)

    def reachable(self, node):
        self.seen.add(node)

        for next_node in self.graph[node]:
            if next_node in self.seen:
                return False
            if not self.reachable(next_node):
                return False

        self.seen.discard(node)

        return len(self.graph[node]) != 0 or node == self.destination
