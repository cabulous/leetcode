from typing import List


# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/discuss/322961/Python-Union-Find
class Solution:

    def __init__(self):
        self.parents = {}
        self.groups = 0

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        self.parents = {x: x for x in range(n)}
        self.groups = n

        for time, x, y in sorted(logs):
            self.union(x, y)
            if self.groups == 1:
                return time

        return -1

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.groups -= 1
            self.parents[root_y] = root_x
