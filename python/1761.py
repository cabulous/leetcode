from collections import defaultdict
from typing import List


# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/discuss/1064783/TLE-one-idea-to-shorten-run-time-from-11-s-to-0.7-s-for-Python-3...
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        degree_nodes = sorted([len(graph[node]), node] for node in graph)
        res = float('inf')

        for node1, node2 in edges:
            for in_degree, node in degree_nodes:
                is_connect_node1 = node in graph[node1]
                is_connect_node2 = node in graph[node2]
                if is_connect_node1 and is_connect_node2:
                    res = min(res, len(graph[node1]) + len(graph[node2]) + in_degree)
                    break

        return res - 6 if res != float('inf') else -1
