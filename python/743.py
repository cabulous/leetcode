import heapq
import math
from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/network-delay-time/discuss/187713/Python-concise-queue-and-heap-solutions
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))

        min_time = [math.inf] * (n + 1)
        min_time[0] = 0
        queue = deque([(0, k)])

        while queue:
            time, node = queue.popleft()
            if time < min_time[node]:
                min_time[node] = time
                for next_node, next_time in graph[node]:
                    queue.append((time + next_time, next_node))

        res = max(min_time)

        return res if res < math.inf else -1


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))

        queue = [(0, k)]
        visited_time = {}

        while queue:
            time, node = heapq.heappop(queue)
            if node not in visited_time:
                visited_time[node] = time
                for target, delta_time in graph[node]:
                    heapq.heappush(queue, (time + delta_time, target))

        return max(visited_time.values()) if len(visited_time) == n else -1
