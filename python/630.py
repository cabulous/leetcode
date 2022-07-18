import heapq
from typing import List


# https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        course_group = sorted(courses, key=lambda x: [x[1], x[0]])

        taken = []
        total_time = 0

        for time, end in course_group:
            heapq.heappush(taken, -time)
            total_time += time
            if total_time > end:
                largest_time = -heapq.heappop(taken)
                total_time -= largest_time

        return len(taken)
