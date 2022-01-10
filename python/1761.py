from collections import defaultdict
from typing import List


# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/discuss/1064783/TLE-one-idea-to-shorten-run-time-from-11-s-to-0.7-s-for-Python-3...
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        degree_node = sorted([[len(graph[k]), k] for k in graph])
        res = float('inf')

        for u, v in edges:
            in_degree_sum = len(graph[u]) + len(graph[v])
            for in_degree, node in degree_node:
                if node in graph[u] and node in graph[v]:
                    res = min(res, in_degree_sum + in_degree)
                    break

        return res - 6 if res != float('inf') else -1
