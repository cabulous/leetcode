from typing import List
from collections import defaultdict


# https://leetcode.com/problems/kill-process/discuss/103170/Simple-Python-BFS-Solution
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = defaultdict(list)
        for c, p in zip(pid, ppid):
            d[p].append(c)
        bfs = [kill]
        for i in bfs:
            bfs.extend(d[i])
        return bfs
