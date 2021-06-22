from typing import List
from collections import defaultdict


# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/discuss/304940/Python-straightforward-DFS
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen = set()

        for v, w in edges:
            graph[v].append(w)

        def dfs(curr_node):
            seen.add(curr_node)
            for next_node in graph[curr_node]:
                if next_node == curr_node or next_node in seen:
                    return False
                if not dfs(next_node):
                    return False
            seen.discard(curr_node)
            return len(graph[curr_node]) != 0 or curr_node == destination

        return dfs(source)
