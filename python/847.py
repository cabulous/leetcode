from collections import deque


# https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/178744/Python-BFS-solution-with-optimization.-Beats-100
class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        masks = [1 << i for i in range(len(graph))]
        visited_state = [{masks[i]} for i in range(len(graph))]
        all_visited = (1 << len(graph)) - 1
        queue = deque([(i, masks[i]) for i in range(len(graph))])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                node, visited = queue.popleft()
                if visited == all_visited:
                    return steps
                for next_node in graph[node]:
                    next_state = visited | masks[next_node]
                    if next_state == all_visited:
                        return steps + 1
                    if next_state not in visited_state[next_node]:
                        visited_state[next_node].add(next_state)
                        queue.append((next_node, next_state))
            steps += 1

        return -1
