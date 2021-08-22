from typing import List


# https://leetcode.com/problems/graph-valid-tree/discuss/69020/8-10-lines-Union-Find-DFS-and-BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            return x if x == parent[x] else find(parent[x])

        def union(xy):
            x, y = map(find, xy)
            parent[x] = y
            return x != y

        return all(map(union, edges))


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v].append(w)
            neighbors[w].append(v)

        stack = [0]
        while stack:
            stack += neighbors.pop(stack.pop(), [])

        return not neighbors


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        parent = {0: -1}
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in adj_list[node]:
                if nei == parent[node]:
                    continue
                if nei in parent:
                    return False
                parent[nei] = node
                stack.append(nei)

        return len(parent) == n


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        seen = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in adj_list[node]:
                if nei in seen:
                    continue
                seen.add(nei)
                stack.append(nei)

        return len(seen) == n
