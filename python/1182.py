import bisect
from typing import List
from collections import defaultdict


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        colors_idx_map = defaultdict(list)
        for i, color in enumerate(colors):
            colors_idx_map[color].append(i)

        res = []
        for target, color in queries:
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
        dist = [[-1] * len(colors) for _ in range(3)]

        right_most = [0] * 3
        for right in range(len(colors)):
            color = colors[right] - 1
            for left in range(right_most[color], right + 1):
                dist[color][left] = right - left
            right_most[color] = right

        left_most = [len(colors) - 1] * 3
        for left in range(len(colors) - 1, -1, -1):
            color = colors[left] - 1
            for right in range(left_most[color], left - 1, -1):
                if dist[color][right] == -1 or dist[color][right] > right - left:
                    dist[color][right] = right - left
            left_most[color] = left

        return [dist[c - 1][i] for i, c in queries]
