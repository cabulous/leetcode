from typing import List
from collections import defaultdict


# https://leetcode.com/problems/prefix-and-suffix-search/solution/551448
class WordFilter:
    Trie = lambda: defaultdict(WordFilter.Trie)
    WEIGHT = 'weight'

    def __init__(self, words: List[str]):
        self.trie = WordFilter.Trie()
        for weight, word in enumerate(words):
            for i in range(len(word) + 1):
                node = self.trie
                node[WordFilter.WEIGHT] = weight
                word_to_insert = word[i:] + '#' + word
                for c in word_to_insert:
                    node = node[c]
                    node[WordFilter.WEIGHT] = weight

    def f(self, prefix: str, suffix: str) -> int:
        node = self.trie
        for c in suffix + '#' + prefix:
            if c not in node:
                return -1
            node = node[c]
        return node[WordFilter.WEIGHT]
