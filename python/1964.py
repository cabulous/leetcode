import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        mono = []
        res = []

        for num in obstacles:
            i = bisect.bisect_right(mono, num)
            res.append(i + 1)
            if i == len(mono):
                mono.append(0)
            mono[i] = num

        return res
