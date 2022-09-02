from itertools import product


class Solution:
    def nextClosestTime(self, time: str) -> str:
        nums = time.replace(':', '')
        candidates = set()

        for cand in product(nums, repeat=4):
            d1, d2, d3, d4 = cand
            if f'{d1}{d2}' < '24' and d3 < '6':
                candidates.add(f'{d1}{d2}:{d3}{d4}')

        res = sorted(candidates)
        idx = res.index(time)

        return res[idx + 1] if idx + 1 < len(res) else res[0]
