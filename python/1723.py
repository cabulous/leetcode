from typing import List


# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1010057/JavaPython-Binary-Search-100
class Solution:

    def __init__(self):
        self.jobs = []
        self.k = 0

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        self.jobs = jobs
        self.k = k

        left, right = max(jobs), sum(jobs)
        while left <= right:
            mid = left + (right - left) // 2
            cap = [mid] * k
            if self.dfs(0, cap, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def dfs(self, i, cap, target):
        if i == len(self.jobs):
            return True

        for j in range(self.k):
            if cap[j] >= self.jobs[i]:
                cap[j] -= self.jobs[i]
                if self.dfs(i + 1, cap, target):
                    return True
                cap[j] += self.jobs[i]
            if cap[j] == target:
                break

        return False
