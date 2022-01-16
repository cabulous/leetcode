import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = []
        intervals.sort(key=lambda x: x[0])
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

        used_rooms = 0
        start_times = sorted(start for start, _ in intervals)
        end_times = sorted(end for _, end in intervals)
        start_pointer = end_pointer = 0

        while start_pointer < len(intervals):
            if end_times[end_pointer] <= start_times[start_pointer]:
                used_rooms -= 1
                end_pointer += 1
            used_rooms += 1
            start_pointer += 1

        return used_rooms
