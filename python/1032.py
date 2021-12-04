from collections import deque
from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque()

        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie

        for c in self.stream:
            if '$' in node:
                return True
            if c not in node:
                return False
            node = node[c]

        return '$' in node
