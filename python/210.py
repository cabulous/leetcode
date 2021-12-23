from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        adj_list = defaultdict(list)
        in_degree = {}

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] = in_degree.get(dest, 0) + 1

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


# https://leetcode.com/problems/course-schedule-ii/discuss/59455/Fast-python-DFS-solution-with-inline-explanation
class Solution:
    def __init__(self):
        self.graph = []
        self.visited = []
        self.res = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        self.graph = defaultdict(list)
        for u, v in prerequisites:
            self.graph[u].append(v)

        self.visited = [0] * numCourses

        for i in range(numCourses):
            if not self.dfs(i):
                return []

        return self.res

    def dfs(self, node):
        if self.visited[node] == -1:
            return False

        if self.visited[node] == 1:
            return True

        self.visited[node] = -1

        for i in self.graph[node]:
            if not self.dfs(i):
                return False

        self.visited[node] = 1
        self.res.append(node)

        return True
