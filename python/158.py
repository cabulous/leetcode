from collections import deque
from typing import List


def read4(buf4: List[str]) -> int:
    pass


# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/193873/Most-elegant-and-simple-solution-in-Python
class Solution:

    def __init__(self):
        self.queue = deque()

    def read(self, buf: List[str], n: int) -> int:
        i = 0

        while i < n:
            if self.queue:
                buf[i] = self.queue.popleft()
                i += 1
            else:
                temp_buf = [''] * 4
                size = read4(temp_buf)
                if size == 0:
                    break
                self.queue.extend(temp_buf[:size])

        return i
