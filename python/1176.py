from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        total = sum(calories[:k])
        res = 0
        if total < lower:
            res -= 1
        elif upper < total:
            res += 1

        for i in range(k, len(calories)):
            total += calories[i] - calories[i - k]
            if total < lower:
                res -= 1
            elif upper < total:
                res += 1

        return res


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        prefix_sum = [0]
        for num in calories:
            prefix_sum.append(prefix_sum[-1] + num)

        res = 0
        for i in range(len(calories) - k + 1):
            total = prefix_sum[i + k] - prefix_sum[i]
            if total < lower:
                res -= 1
            elif upper < total:
                res += 1

        return res
