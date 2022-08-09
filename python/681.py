from itertools import product


class Solution:
    def nextClosestTime(self, time: str) -> str:
        nums = time.replace(':', '')
        candidates = set()

        for cand in product(nums, repeat=4):
            d1, d2, d3, d4 = cand
            if f'{d1}{d2}' < '24' and d3 < '6':
                candidates.add(f'{d1}{d2}:{d3}{d4}')

        res = sorted(list(candidates))
        idx = res.index(time)

        return res[idx + 1] if idx + 1 < len(res) else res[0]


# https://leetcode.com/problems/next-closest-time/discuss/190816/Python-simple-20ms-solution
class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(':')
        nums = sorted(set(hour + minute))
        two_digit = [a + b for a in nums for b in nums]

        minute_idx = two_digit.index(minute)
        if minute_idx + 1 < len(two_digit) and two_digit[minute_idx + 1] < '60':
            return hour + ':' + two_digit[minute_idx + 1]

        hour_idx = two_digit.index(hour)
        if hour_idx + 1 < len(two_digit) and two_digit[hour_idx + 1] < '24':
            return two_digit[hour_idx + 1] + ':' + two_digit[0]

        return two_digit[0] + ':' + two_digit[0]
