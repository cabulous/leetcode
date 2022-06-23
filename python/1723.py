from typing import List


# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1010057/JavaPython-Binary-Search-100
class Solution:

    def __init__(self):
        self.jobs = []

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        self.jobs = jobs

        left, right = max(jobs), sum(jobs)
        while left <= right:
            mid = left + (right - left) // 2
            if self.can_reach(0, [mid] * k, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def can_reach(self, job_idx, bucket, origin_val):
        if job_idx == len(self.jobs):
            return True

        for i in range(len(bucket)):
            if bucket[i] >= self.jobs[job_idx]:
                bucket[i] -= self.jobs[job_idx]
                if self.can_reach(job_idx + 1, bucket, origin_val):
                    return True
                bucket[i] += self.jobs[job_idx]
            if bucket[i] == origin_val:
                return False

        return False
