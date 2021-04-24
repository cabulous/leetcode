from typing import List
from collections import defaultdict


# https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me/419605
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        low = [0] * n
        edges = defaultdict(list)

        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)

        def dfs(rank, curr, prev):
            low[curr] = rank
            res = []
            for neighbor in edges[curr]:
                if neighbor == prev:
                    continue
                if not low[neighbor]:
                    res += dfs(rank + 1, neighbor, curr)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] >= rank + 1:
                    res.append([curr, neighbor])
            return res

        return dfs(1, 0, -1)


class Solution:
    def __init__(self):
        self.rank = {}
        self.graph = defaultdict(list)
        self.conn_dict = {}

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.form_graph(n, connections)
        self.dfs(0, 0)

        res = []
        for u, v in self.conn_dict:
            res.append([u, v])

        return res

    def dfs(self, node, discovery_rank):
        if self.rank[node]:
            return self.rank[node]
        self.rank[node] = discovery_rank
        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)
            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]
            min_rank = min(min_rank, recursive_rank)
        return min_rank

    def form_graph(self, n, connections):
        for i in range(n):
            self.rank[i] = None

        for edge in connections:
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.conn_dict[(min(u, v), max(u, v))] = 1
