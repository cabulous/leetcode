import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted((start, process, idx) for idx, (start, process) in enumerate(tasks))

        available_tasks = []
        curr_time = 0
        curr_task_idx = 0
        res = []

        while curr_task_idx < len(sorted_tasks) or available_tasks:
            if not available_tasks and curr_time < sorted_tasks[curr_task_idx][0]:
                curr_time = sorted_tasks[curr_task_idx][0]

            while curr_task_idx < len(sorted_tasks) and sorted_tasks[curr_task_idx][0] <= curr_time:
                _, process, idx = sorted_tasks[curr_task_idx]
                heapq.heappush(available_tasks, (process, idx))
                curr_task_idx += 1

            next_process, next_idx = heapq.heappop(available_tasks)
            curr_time += next_process
            res.append(next_idx)

        return res
