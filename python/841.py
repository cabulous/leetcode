from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [True] + [False] * (len(rooms) - 1)
        queue = deque([0])

        while queue:
            idx = queue.popleft()
            for key in rooms[idx]:
                if not seen[key]:
                    seen[key] = True
                    queue.append(key)

        return all(seen)
