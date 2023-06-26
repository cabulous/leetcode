import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        head_queue = costs[:candidates]
        tail_queue = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(head_queue)
        heapq.heapify(tail_queue)

        head_reader = candidates
        tail_reader = len(costs) - candidates - 1
        res = 0

        for _ in range(k):
            if not tail_queue or (head_queue and head_queue[0] <= tail_queue[0]):
                res += heapq.heappop(head_queue)
                if head_reader <= tail_reader:
                    heapq.heappush(head_queue, costs[head_reader])
                    head_reader += 1
            else:
                res += heapq.heappop(tail_queue)
                if head_reader <= tail_reader:
                    heapq.heappush(tail_queue, costs[tail_reader])
                    tail_reader -= 1

        return res
