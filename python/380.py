from random import choice


class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_elem, idx = self.list[-1], self.dict[val]
        self.list[idx], self.dict[last_elem] = last_elem, idx
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.list)
