from collections import defaultdict
from typing import List


# https://leetcode.com/problems/minimum-height-trees/discuss/76132/Iterative-remove-leaves-Python-solution
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        res = set(range(n))
        while len(res) > 2:
            leaves = set(i for i in res if len(graph[i]) == 1)
            res -= leaves
            for i in leaves:
                for j in graph[i]:
                    graph[j].remove(i)

        return list(res)
