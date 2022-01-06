class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


# https://leetcode.com/problems/employee-free-time/discuss/170551/Simple-Python-9-liner-beats-97-(with-explanation)
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        flatten_schedule = [i for s in schedule for i in s]
        flatten_schedule.sort(key=lambda x: x.start)

        prev = flatten_schedule[0]
        res = []

        for curr in flatten_schedule[1:]:
            if curr.start <= prev.end < curr.end:
                prev.end = curr.end
            elif curr.start > prev.end:
                res.append(Interval(prev.end, curr.start))
                prev = curr

        return res
