import heapq


# https://leetcode.com/problems/max-stack/discuss/309621/Python-using-stack-%2B-heap-%2B-set-with-explanation-and-discussion-of-performance
class MaxStack:

    def __init__(self):
        self.soft_delete = set()
        self.max_heap = []
        self.recency_stack = []
        self.next_id = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.max_heap, (-x, self.next_id))
        self.recency_stack.append((x, self.next_id))
        self.next_id -= 1

    def _clean_up(self):
        while self.max_heap and self.max_heap[0][1] in self.soft_delete:
            self.soft_delete.remove(heapq.heappop(self.max_heap)[1])
        while self.recency_stack and self.recency_stack[-1][1] in self.soft_delete:
            self.soft_delete.remove(self.recency_stack.pop()[1])

    def pop(self) -> int:
        val, curr_id = self.recency_stack.pop()
        self.soft_delete.add(curr_id)
        self._clean_up()
        return val

    def top(self) -> int:
        return self.recency_stack[-1][0]

    def peekMax(self) -> int:
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        neg_val, curr_id = heapq.heappop(self.max_heap)
        self.soft_delete.add(curr_id)
        self._clean_up()
        return -neg_val
