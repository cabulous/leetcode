from collections import deque
from functools import lru_cache


# dfs
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x + y == 0:
                return 0
            if x + y == 2:
                return 2
            return 1 + min(
                dfs(abs(x - 1), abs(y - 2)),
                dfs(abs(x - 2), abs(y - 1)),
            )

        return dfs(abs(x), abs(y))


# bfs
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x, y):
            visited = set()
            queue = deque([(0, 0)])
            steps = 0
            while queue:
                curr_level_cnt = len(queue)
                for i in range(curr_level_cnt):
                    cx, cy = queue.popleft()
                    if (cx, cy) == (x, y):
                        return steps
                    for dx, dy in offsets:
                        nx, ny = cx + dx, cy + dy
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                steps += 1

        return bfs(x, y)


# bidirectional bfs
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        origin_queue = deque([(0, 0, 0)])
        origin_distance = {(0, 0): 0}

        target_queue = deque([(x, y, 0)])
        target_distance = {(x, y): 0}

        while True:
            origin_x, origin_y, origin_steps = origin_queue.popleft()
            if (origin_x, origin_y) in target_distance:
                return origin_steps + target_distance[(origin_x, origin_y)]

            target_x, target_y, target_steps = target_queue.popleft()
            if (target_x, target_y) in origin_distance:
                return target_steps + origin_distance[(target_x, target_y)]

            for dx, dy in offsets:
                next_origin_x, next_origin_y = origin_x + dx, origin_y + dy
                if (next_origin_x, next_origin_y) not in origin_distance:
                    origin_queue.append((next_origin_x, next_origin_y, origin_steps + 1))
                    origin_distance[(next_origin_x, next_origin_y)] = origin_steps + 1

                next_target_x, next_target_y = target_x + dx, target_y + dy
                if (next_target_x, next_target_y) not in target_distance:
                    target_queue.append((next_target_x, next_target_y, target_steps + 1))
                    target_distance[(next_target_x, next_target_y)] = target_steps + 1
