from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return ans


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        hottest = 0

        for curr_day in reversed(range(len(temperatures))):
            curr_temp = temperatures[curr_day]
            if curr_temp >= hottest:
                hottest = curr_temp
                continue
            days = 1
            while temperatures[curr_day + days] <= curr_temp:
                days += ans[curr_day + days]
            ans[curr_day] = days

        return ans
