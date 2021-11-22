from collections import OrderedDict
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = OrderedDict()
        self.is_unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.queue:
            return next(iter(self.queue))
        return -1

    def add(self, value: int) -> None:
        if value not in self.is_unique:
            self.is_unique[value] = True
            self.queue[value] = None
        elif self.is_unique[value]:
            self.is_unique[value] = False
            self.queue.pop(value)
