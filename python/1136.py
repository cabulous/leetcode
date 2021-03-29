from typing import List


# dfs
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for start_node, end_node in relations:
            graph[start_node].append(end_node)

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = -1
            max_length = 1
            for end_node in graph[node]:
                length = dfs(end_node)
                if length == -1:
                    return -1
                max_length = max(max_length, length + 1)
            visited[node] = max_length
            return max_length

        max_length = -1

        for start_node in graph:
            length = dfs(start_node)
            if length == -1:
                return -1
            max_length = max(max_length, length)

        return max_length


# bfs
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        in_degree = {i: 0 for i in range(1, n + 1)}

        for start_node, end_node in relations:
            graph[start_node].append(end_node)
            in_degree[end_node] += 1

        queue = []

        for node in graph:
            if in_degree[node] == 0:
                queue.append(node)

        step = 0
        studied_count = 0

        while queue:
            step += 1
            next_queue = []
            for node in queue:
                studied_count += 1
                for end_node in graph[node]:
                    in_degree[end_node] -= 1
                    if in_degree[end_node] == 0:
                        next_queue.append(end_node)
            queue = next_queue

        return step if studied_count == n else -1
