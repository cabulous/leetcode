from typing import List


# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/77625/Short-Union-Find-in-Python-Ruby-C%2B%2B
# Union Find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = list(range(n))

        def find(v):
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]

        for v, w in edges:
            p[find(v)] = find(w)

        return len(set(map(find, p)))


# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/77638/Python-DFS-BFS-Union-Find-solutions
# dfs
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        g = {x: [] for x in range(n)}
        res = 0

        for v, w in edges:
            g[v].append(w)
            g[w].append(v)

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for x in g[node]:
                dfs(x)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1

        return res


# bfs
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {x: [] for x in range(n)}
        res = 0

        for v, w in edges:
            g[v].append(w)
            g[w].append(v)

        for i in range(n):
            queue = [i]
            res += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return res
