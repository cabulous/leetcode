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

        return not any(self.find(x) == self.find(y) for x, eq, _, y in equations if eq == '!')

    def find(self, x):
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.uf[root_x] = root_y
