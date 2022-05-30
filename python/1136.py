from collections import defaultdict
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        in_degree = defaultdict(int)

        for start, end in relations:
            graph[start].append(end)
            in_degree[end] += 1

        queue = [node for node in graph if in_degree[node] == 0]
        step = 0
        studied_count = 0

        while queue:
            step += 1
            next_queue = []
            for node in queue:
                studied_count += 1
                for next_node in graph[node]:
                    in_degree[next_node] -= 1
                    if in_degree[next_node] == 0:
                        next_queue.append(next_node)
            queue = next_queue

        return step if studied_count == n else -1
