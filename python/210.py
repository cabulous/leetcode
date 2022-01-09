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
            course = zero_in_degree.popleft()
            res.append(course)
            if course not in adj_list:
                continue
            for next_course in adj_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    zero_in_degree.append(next_course)

        return res if len(res) == numCourses else []
