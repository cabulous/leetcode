import heapq
from typing import List


# https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        lst = list(map(lambda x: [x[1], x[0]], courses))
        lst.sort()
        pq = []
        cnt = 0
        for end, t in lst:
            cnt += t
            heapq.heappush(pq, -t)
            if cnt > end:
                cnt += heapq.heappop(pq)
        return len(pq)
