import heapq
from collections import deque
from math import inf
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)

        score = [0] * n
        score[0] = nums[0]

        dq = deque([0])

        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()
            score[i] = score[dq[0]] + nums[i]
            while dq and score[dq[-1]] <= score[i]:
                dq.pop()
            dq.append(i)

        return score[-1]


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = nums[0]

        priority_queue = []
        heapq.heappush(priority_queue, (-score, 0))

        for i in range(1, n):
            while priority_queue[0][1] < i - k:
                heapq.heappop(priority_queue)
            score = nums[i] - priority_queue[0][0]
            heapq.heappush(priority_queue, (-score, i))

        return score


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tree = [0] * (n * 2)

        self.update(0, nums[0], tree, n)

        for i in range(1, n):
            max_value = self.query(max(0, i - k), i, tree, n)
            self.update(i, max_value + nums[i], tree, n)

        return tree[-1]

    def update(self, index, value, tree, size):
        index += size
        tree[index] = value
        while index > 1:
            index >>= 1
            tree[index] = max(tree[index << 1], tree[(index << 1) + 1])

    def query(self, left, right, tree, size):
        res = -inf
        left += size
        right += size
        while left < right:
            if left & 1:
                res = max(res, tree[left])
                left += 1
            left >>= 1
            if right & 1:
                right -= 1
                res = max(res, tree[right])
            right >>= 1
        return res
