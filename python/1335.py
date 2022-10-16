from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        min_diff = [[float('inf')] * len(jobDifficulty) + [0] for _ in range(d + 1)]

        for days_remaining in range(1, d + 1):
            for i in range(len(jobDifficulty) - days_remaining + 1):
                daily_max_job_diff = 0
                for j in range(i + 1, len(jobDifficulty) - days_remaining + 2):
                    daily_max_job_diff = max(daily_max_job_diff, jobDifficulty[j - 1])
                    min_diff[days_remaining][i] = min(
                        min_diff[days_remaining][i],
                        daily_max_job_diff + min_diff[days_remaining - 1][j],
                    )

        if min_diff[d][0] == float('inf'):
            return -1

        return min_diff[d][0]
