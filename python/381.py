from collections import defaultdict
from random import choice


class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False

        remove_idx = self.idx[val].pop()
        last_val = self.lst[-1]
        self.lst[remove_idx] = last_val
        self.idx[last_val].add(remove_idx)
        self.idx[last_val].discard(len(self.lst) - 1)

        self.lst.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.lst)
