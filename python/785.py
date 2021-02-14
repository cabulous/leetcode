from typing import List
from collections import deque


# https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution/800016
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(x, c):
            if x in color:
                return color[x] == c
            color[x] = c
            return all(dfs(y, -c) for y in graph[x])

        return all(i in color or dfs(i, 1) for i in range(len(graph)))


# https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution/800016
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def bfs(x):
            q = deque([x])
            color[x] = 1
            while q:
                cur = q.popleft()
                for n in graph[cur]:
                    if n not in color:
                        color[n] = -color[cur]
                        q.append(n)
                    elif color[n] == color[cur]:
                        return False
            return True

        return all(i in color or bfs(i) for i in range(len(graph)))
