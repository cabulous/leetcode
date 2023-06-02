from collections import defaultdict


class Solution:

    def __init__(self):
        self.graph = defaultdict(list)

    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and self.is_in_range(bombs[i], bombs[j]):
                    self.graph[i].append(j)

        res = 0
        for i in range(len(bombs)):
            group = {i}
            self.dfs(i, group)
            res = max(res, len(group))

        return res

    def dfs(self, node, group):
        for next_node in self.graph[node]:
            if next_node not in group:
                group.add(next_node)
                self.dfs(next_node, group)

    def is_in_range(self, bomb1, bomb2):
        x1, y1, r1 = bomb1
        x2, y2, r2 = bomb2
        return r1 ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2
