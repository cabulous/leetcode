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
            time = [mid] * k
            if self.can_reach(0, time, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def can_reach(self, curr_job_index, time, target):
        if curr_job_index == len(self.jobs):
            return True

        for i in range(self.k):
            if time[i] >= self.jobs[curr_job_index]:
                time[i] -= self.jobs[curr_job_index]
                if self.can_reach(curr_job_index + 1, time, target):
                    return True
                time[i] += self.jobs[curr_job_index]
            if time[i] == target:
                break

        return False
