from typing import List


# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1010057/JavaPython-Binary-Search-100
class Solution:

    def __init__(self):
        self.jobs = []
        self.bucket_count = 0

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        self.jobs = jobs
        self.bucket_count = k

        left, right = max(jobs), sum(jobs)
        while left <= right:
            mid = left + (right - left) // 2
            if self.can_reach(0, [mid] * k, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def can_reach(self, curr_job_index, bucket, origin_val):
        if curr_job_index == len(self.jobs):
            return True

        for i in range(self.bucket_count):
            if bucket[i] >= self.jobs[curr_job_index]:
                bucket[i] -= self.jobs[curr_job_index]
                if self.can_reach(curr_job_index + 1, bucket, origin_val):
                    return True
                bucket[i] += self.jobs[curr_job_index]
            if bucket[i] == origin_val:
                return False

        return False