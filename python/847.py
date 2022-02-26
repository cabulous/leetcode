from collections import deque
from typing import List


# https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/178744/Python-BFS-solution-with-optimization.-Beats-100
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        node_count = len(graph)
        masks = [1 << i for i in range(node_count)]
        all_visited = (1 << node_count) - 1
        visited_state = [{masks[i]} for i in range(node_count)]
        queue = deque([(i, masks[i]) for i in range(node_count)])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                node, visited = queue.popleft()
                if visited == all_visited:
                    return steps
                for next_node in graph[node]:
                    new_visited = visited | masks[next_node]
                    if new_visited == all_visited:
                        return steps + 1
                    if new_visited not in visited_state[next_node]:
                        visited_state[next_node].add(new_visited)
                        queue.append((next_node, new_visited))
            steps += 1

        return -1
