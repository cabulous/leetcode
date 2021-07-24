from typing import List
from collections import defaultdict


# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/discuss/304940/Python-straightforward-DFS
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen = set()

        for u, v in edges:
            graph[u].append(v)

        def reachable(node):
            seen.add(node)
            for nei in graph[node]:
                if nei == node or nei in seen:
                    return False
                if not reachable(nei):
                    return False
            seen.discard(node)
            return len(graph[node]) != 0 or node == destination

        return reachable(source)
