from typing import List


class Solution:

    def __init__(self):
        self.k = 0
        self.res = []

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))

        self.k = k

        for num in range(1, 10):
            self.dfs(n - 1, num)

        return self.res

    def dfs(self, n, num):
        if n == 0:
            self.res.append(num)
            return

        tail_digit = num % 10
        next_digits = {tail_digit - self.k, tail_digit + self.k}
        for nd in next_digits:
            if 0 <= nd < 10:
                self.dfs(n - 1, num * 10 + nd)


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))

        queue = list(range(1, 10))
        for _ in range(n - 1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                next_digits = {tail_digit - k, tail_digit + k}
                for nd in next_digits:
                    if 0 <= nd < 10:
                        next_queue.append(num * 10 + nd)
            queue = next_queue

        return queue
