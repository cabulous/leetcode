import string
from typing import List


# https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/234486/JavaC%2B%2BPython-Easy-Union-Find
class Solution:

    def __init__(self):
        self.uf = {x: x for x in string.ascii_lowercase}

    def equationsPossible(self, equations: List[str]) -> bool:
        for x, eq, _, y in equations:
            if eq == '=':
                self.union(x, y)

        return not any(eq == '!' and self.find(x) == self.find(y) for x, eq, _, y in equations)

    def find(self, x):
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.uf[root_x] = root_y


class Solution:

    def __init__(self):
        self.graph = [[] for _ in range(26)]
        self.node_color = [-1] * 26

    def equationsPossible(self, equations: List[str]) -> bool:
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[-1]) - ord('a')
                self.graph[x].append(y)
                self.graph[y].append(x)

        for i in range(26):
            if self.node_color[i] == -1:
                self.dfs(i, i)

        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[-1]) - ord('a')
                if self.node_color[x] == self.node_color[y]:
                    return False

        return True

    def dfs(self, node, color):
        if self.node_color[node] == -1:
            self.node_color[node] = color
            for next_node in self.graph[node]:
                self.dfs(next_node, color)
