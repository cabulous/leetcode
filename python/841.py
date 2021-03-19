from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [True] + [False] * (len(rooms) - 1)
        stack = [0]
        while stack:
            idx = stack.pop()
            for key in rooms[idx]:
                if not seen[key]:
                    seen[key] = True
                    stack.append(key)
        return all(seen)
