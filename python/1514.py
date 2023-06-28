from collections import defaultdict, deque


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        dest_prob = [0.0] * n
        dest_prob[start] = 1.0

        queue = deque([start])
        while queue:
            node = queue.popleft()
            for next_node, prob in graph[node]:
                next_prob = dest_prob[node] * prob
                if next_prob > dest_prob[next_node]:
                    dest_prob[next_node] = next_prob
                    queue.append(next_node)

        return dest_prob[end]
