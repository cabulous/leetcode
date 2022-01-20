import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        used_rooms = []
        heapq.heappush(used_rooms, intervals[0][1])

        for start, end in intervals[1:]:
            if used_rooms[0] <= start:
                heapq.heappop(used_rooms)
            heapq.heappush(used_rooms, end)

        return len(used_rooms)


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        start_times = sorted(start for start, _ in intervals)
        end_times = sorted(end for _, end in intervals)
        start_ptr = end_ptr = 0
        used_rooms = 0

        while start_ptr < len(start_times):
            if end_times[end_ptr] <= start_times[start_ptr]:
                used_rooms -= 1
                end_ptr += 1
            used_rooms += 1
            start_ptr += 1

        return used_rooms
