import random
from typing import List


# https://leetcode.com/problems/random-pick-with-blacklist/discuss/146533/Super-Simple-Python-AC-w-Remapping
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        blacklist = set(blacklist)

        self.length = n - len(blacklist)
        self.remap = {}

        need_remap = []
        for num in blacklist:
            if num < self.length:
                need_remap.append(num)

        j = 0
        for i in range(self.length, n):
            if i not in blacklist:
                self.remap[need_remap[j]] = i
                j += 1

    def pick(self) -> int:
        index = random.randrange(self.length)
        if index in self.remap:
            return self.remap[index]
        return index
