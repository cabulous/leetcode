import bisect
from typing import List
from collections import defaultdict


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        colors_idx_map = defaultdict(list)
        for i, c in enumerate(colors):
            colors_idx_map[c].append(i)

        res = []
        for i, (target, color) in enumerate(queries):
            if color not in colors_idx_map:
                res.append(-1)
                continue

            idx_list = colors_idx_map[color]
            insert = bisect.bisect_left(idx_list, target)
            left_nearest = abs(idx_list[max(insert - 1, 0)] - target)
            right_nearest = abs(idx_list[min(insert, len(idx_list) - 1)] - target)

            res.append(min(left_nearest, right_nearest))

        return res


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        rightmost = [0, 0, 0]
        leftmost = [n - 1, n - 1, n - 1]
        dist = [[-1] * n for _ in range(3)]

        for i in range(n):
            color = colors[i] - 1
            for j in range(rightmost[color], i + 1):
                dist[color][j] = i - j
            rightmost[color] = i

        for i in range(n - 1, -1, -1):
            color = colors[i] - 1
            for j in range(leftmost[color], i - 1, -1):
                if dist[color][j] == -1 or dist[color][j] > j - i:
                    dist[color][j] = j - i
            leftmost[color] = i

        return [dist[c - 1][i] for i, c in queries]
