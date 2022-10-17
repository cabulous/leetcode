from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        global_min = [[float('inf')] * len(jobDifficulty) + [0] for _ in range(d + 1)]

        for days_remaining in range(1, d + 1):
            for i in range(len(jobDifficulty) - days_remaining + 1):
                local_max = 0
                for j in range(i + 1, len(jobDifficulty) - days_remaining + 2):
                    local_max = max(local_max, jobDifficulty[j - 1])
                    global_min[days_remaining][i] = min(
                        global_min[days_remaining][i],
                        local_max + global_min[days_remaining - 1][j],
                    )

        if global_min[d][0] == float('inf'):
            return -1

        return global_min[d][0]
