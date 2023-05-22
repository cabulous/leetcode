import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = sorted(intervals, key=lambda x: x[0])

        used_rooms = []
        heapq.heappush(used_rooms, meetings[0][1])

        for start, end in meetings[1:]:
            if used_rooms[0] <= start:
                heapq.heappop(used_rooms)
            heapq.heappush(used_rooms, end)

        return len(used_rooms)
