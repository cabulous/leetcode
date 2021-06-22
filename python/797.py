from collections import deque
from functools import lru_cache
from typing import List


# backtracking
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []

        def backtrack(curr_node, path):
            if curr_node == target:
                results.append(list(path))
                return
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        path = deque([0])
        backtrack(0, path)

        return results


# dp
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1

        @lru_cache(None)
        def all_paths_to_target(curr_node):
            if curr_node == target:
                return [[target]]

            results = []

            for next_node in graph[curr_node]:
                for path in all_paths_to_target(next_node):
                    results.append([curr_node] + path)

            return results

        return all_paths_to_target(0)
