from collections import defaultdict
from typing import List


# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/solutions/3042992/python3-dfs-explained/
class Solution:

    def __init__(self):
        self.s = ''
        self.graph = defaultdict(list)
        self.res = 1

    def longestPath(self, parent: List[int], s: str) -> int:
        self.s = s

        for end, start in enumerate(parent):
            self.graph[start].append(end)

        self.dfs(0)

        return self.res

    def dfs(self, curr_node):
        max1 = 0
        max2 = 0

        for next_node in self.graph[curr_node]:
            next_max = self.dfs(next_node)
            if self.s[next_node] != self.s[curr_node]:
                if next_max > max1:
                    max1, max2 = next_max, max1
                elif next_max > max2:
                    max2 = next_max

        self.res = max(self.res, max1 + max2 + 1)

        return max1 + 1
