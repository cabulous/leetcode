# https://leetcode.com/problems/design-skiplist/discuss/393713/Python-1-node-per-value-and-100
import math
import random


class Node:

    def __init__(self, val, levels):
        self.val = val
        self.levels = [None] * levels


class Skiplist:

    def __init__(self):
        self.head = Node(-1, 16)

    def _iter(self, num):
        curr = self.head
        for level in range(15, -1, -1):
            while True:
                future = curr.levels[level]
                if future and future.val < num:
                    curr = future
                else:
                    break
            yield curr, level

    def search(self, target: int) -> bool:
        node = None
        for prev, level in self._iter(target):
            node = prev
        curr = node.levels[0]
        return curr and curr.val == target

    def add(self, num: int) -> None:
        node_levels = min(16, 1 + int(math.log2(1.0 / random.random())))
        node = Node(num, node_levels)

        for curr, level in self._iter(num):
            if level < node_levels:
                future = curr.levels[level]
                curr.levels[level] = node
                node.levels[level] = future

    def erase(self, num: int) -> bool:
        res = False
        for curr, level in self._iter(num):
            future = curr.levels[level]
            if future and future.val == num:
                res = True
                curr.levels[level] = future.levels[level]
        return res
