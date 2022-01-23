from collections import defaultdict


# https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list
class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DLinkedList:

    def __init__(self):
        self._sentinel = Node()
        self._sentinel.prev = self._sentinel.next = self._sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node=None):
        if node is None:
            return
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        node.prev.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return None
        if node is None:
            node = self._sentinel.prev
        node.prev.next, node.next.prev = node.next, node.prev
        self._size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._node = dict()
        self._freq = defaultdict(DLinkedList)
        self._min_freq = 0

    def _update(self, node=None):
        if node is None:
            return
        freq = node.freq
        self._freq[freq].pop(node)
        if self._min_freq == freq and len(self._freq[freq]) == 0:
            self._min_freq += 1
        node.freq += 1
        self._freq[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self._node:
            return -1
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return

        if key in self._node:
            node = self._node[key]
            node.val = value
            self._update(node)
        else:
            if self._size == self._capacity:
                node = self._freq[self._min_freq].pop()
                del self._node[node.key]
                self._size -= 1
            node = Node(key, value)
            self._size += 1
            self._node[key] = node
            self._freq[1].append(node)
            self._min_freq = 1
