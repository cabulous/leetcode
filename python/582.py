from typing import List
from collections import defaultdict


# https://leetcode.com/problems/kill-process/discuss/103170/Simple-Python-BFS-Solution
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        for parent, child in zip(ppid, pid):
            graph[parent].append(child)

        res = []
        queue = [kill]
        while queue:
            next_queue = []
            for node in queue:
                res.append(node)
                for child in graph[node]:
                    next_queue.append(child)
            queue = next_queue

        return res
