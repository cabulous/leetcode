from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = defaultdict(int)

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1

        zero_in_degree = deque([i for i in range(numCourses) if i not in in_degree])
        res = []

        while zero_in_degree:
            vertex = zero_in_degree.popleft()
            res.append(vertex)
            if vertex not in adj_list:
                continue
            for nei in adj_list[vertex]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    zero_in_degree.append(nei)

        return res if len(res) == numCourses else []
