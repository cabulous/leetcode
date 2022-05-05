from collections import deque


# https://leetcode.com/problems/implement-stack-using-queues/discuss/62516/Concise-1-Queue-Java-C%2B%2B-Python
class MyStack:

    def __init__(self):
        self._queue = deque()

    def push(self, x: int) -> None:
        self._queue.appendleft(x)

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return not len(self._queue)
