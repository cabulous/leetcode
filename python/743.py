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
        queue = deque([(k, 0)])

        while queue:
            node, time = queue.popleft()
            if time < min_time[node]:
                min_time[node] = time
                for next_node, next_time in graph[node]:
                    queue.append((next_node, time + next_time))

        res = max(min_time)

        return res if res < math.inf else -1
