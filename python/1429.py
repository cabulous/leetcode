import math
from typing import List


# https://leetcode.com/problems/first-unique-number/discuss/601107/JavaPython-3-DoublyLinkedList-and-LinkedHashSetdict-O(n)-2-neat-codes-w-analysis.
class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.val_to_node = {}
        self.head = Node(-math.inf)
        self.tail = Node(math.inf)
        self.head.next = self.tail
        self.tail.prev = self.head
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        if self.head.next is self.tail:
            return -1
        return self.head.next.val

    def add(self, value: int) -> None:
        if value in self.val_to_node:
            self.remove(self.val_to_node[value])
        else:
            self.val_to_node[value] = Node(value)
            self.move_to_end(self.val_to_node[value])

    def remove(self, node):
        if None in (node.prev, node.next):
            return False
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = node.prev = None
        return True

    def move_to_end(self, node):
        if self.tail.prev is None:
            return False
        node.next, node.prev = self.tail, self.tail.prev
        self.tail.prev, node.prev.next = node, node
        return True
