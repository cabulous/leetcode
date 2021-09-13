import heapq
from typing import List
from collections import defaultdict


# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/discuss/156739/C%2B%2BJavaPython-Dijkstra-%2B-Priority-Queue
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for i, j, l in edges:
            graph[i][j] = graph[j][i] = l

        pq = [(-maxMoves, 0)]
        seen = {}

        while pq:
            moves, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = -moves
                for j in graph[i]:
                    moves2 = -moves - graph[i][j] - 1
                    if j not in seen and moves2 >= 0:
                        heapq.heappush(pq, (-moves2, j))

        res = len(seen)
        for i, j, l in edges:
            res += min(seen.get(i, 0) + seen.get(j, 0), l)

        return res
