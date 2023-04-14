from collections import defaultdict


# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/solutions/1198908/python-shortest-code-and-fast/?orderBy=most_votes
class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * len(colors)
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        zero_in_degree = [i for i in range(len(colors)) if in_degree[i] == 0]
        counts = [[0] * 26 for _ in range(len(colors))]

        while zero_in_degree:
            node = zero_in_degree.pop()
            counts[node][ord(colors[node]) - ord('a')] += 1
            for next_node in graph[node]:
                counts[next_node] = list(map(max, counts[next_node], counts[node]))
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    zero_in_degree.append(next_node)

        if sum(in_degree) > 0:
            return -1

        return max(max(node) for node in counts)
