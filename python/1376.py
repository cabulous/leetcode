from collections import defaultdict, deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        graph = defaultdict(list)
        for v, u in enumerate(manager):
            graph[u].append(v)

        queue = deque([(headID, 0)])
        res = 0
        while queue:
            node, time = queue.popleft()
            res = max(res, time)
            for next_node in graph[node]:
                queue.append((next_node, time + informTime[node]))

        return res
