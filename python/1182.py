import bisect
from typing import List
from collections import defaultdict


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        colors_idx_map = defaultdict(list)
        for i, color in enumerate(colors):
            colors_idx_map[color].append(i)

        res = []
        for i, (target, color) in enumerate(queries):
            if color not in colors_idx_map:
                res.append(-1)
                continue

            idx_list = colors_idx_map[color]
            insert_idx = bisect.bisect_left(idx_list, target)

            left = abs(idx_list[max(0, insert_idx - 1)] - target)
            right = abs(idx_list[min(len(idx_list) - 1, insert_idx)] - target)

            res.append(min(left, right))

        return res


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        dist = [[-1] * n for _ in range(3)]

        right_most = [0, 0, 0]
        for i in range(n):
            color = colors[i] - 1
            for j in range(right_most[color], i + 1):
                dist[color][j] = i - j
            right_most[color] = i

        left_most = [n - 1, n - 1, n - 1]
        for i in range(n - 1, -1, -1):
            color = colors[i] - 1
            for j in range(left_most[color], i - 1, -1):
                if dist[color][j] == -1 or dist[color][j] > j - i:
                    dist[color][j] = j - i
            left_most[color] = i

        return [dist[c - 1][i] for i, c in queries]
