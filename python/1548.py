from collections import defaultdict


# https://leetcode.com/problems/the-most-similar-path-in-a-graph/solutions/790240/python-clean-bottom-up-dp-solution-with-explanation-o-n-2-len-tp/?orderBy=most_votes
class Solution:
    def mostSimilar(self, n: int, roads: list[list[int]], names: list[str], targetPath: list[str]) -> list[int]:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        dist = [[len(targetPath)] * n for _ in range(len(targetPath))]
        prev = [[0] * n for _ in range(len(targetPath))]

        for node in range(n):
            dist[0][node] = (names[node] != targetPath[0])
        for i in range(1, len(targetPath)):
            for node in range(n):
                for next_node in graph[node]:
                    if dist[i - 1][next_node] < dist[i][node]:
                        dist[i][node] = dist[i - 1][next_node]
                        prev[i][node] = next_node
                dist[i][node] += (names[node] != targetPath[i])

        min_dist = len(targetPath)
        res = [0]
        for node in range(n):
            if dist[-1][node] < min_dist:
                min_dist = dist[-1][node]
                res[0] = node
        for i in range(len(targetPath) - 1, 0, -1):
            prev_node = prev[i][res[-1]]
            res.append(prev_node)

        return res[::-1]
