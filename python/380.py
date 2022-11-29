from random import choice


class RandomizedSet:

    def __init__(self):
        self.lookup = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False
        self.lookup[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False

        last_elm = self.list[-1]
        idx = self.lookup[val]
        self.list[idx] = last_elm
        self.lookup[last_elm] = idx

        self.list.pop()
        self.lookup.pop(val)

        return True

    def getRandom(self) -> int:
        return choice(self.list)
