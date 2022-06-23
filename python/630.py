import heapq
from typing import List


# https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        lst = list(map(lambda x: [x[1], x[0]], courses))
        lst.sort()

        taken = []
        total_time = 0

        for end, time in lst:
            total_time += time
            heapq.heappush(taken, -time)
            if total_time > end:
                largest_time = -heapq.heappop(taken)
                total_time -= largest_time

        return len(taken)
