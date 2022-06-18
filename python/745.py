from itertools import product
from typing import List
from collections import defaultdict


# https://leetcode.com/problems/prefix-and-suffix-search/discuss/1185171/Python-Two-solutions-%2B-Trie-and-bruteforce-explained
class TrieNode:

    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.index = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        curr = self.root
        curr.index = index
        for ch in word:
            curr = curr.next[ch]
            curr.index = index

    def starts_with(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.next:
                return -1
            curr = curr.next[ch]
        return curr.index


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.words = {}

        for index, word in enumerate(words):
            long = word + '#' + word
            for i in range(len(word)):
                self.trie.insert(long[i:], index)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.starts_with(suffix + '#' + prefix)


class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            for p, s in product(range(len(word) + 1), repeat=2):
                self.d[word[:p], word[s:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self.d.get((prefix, suffix), -1)
