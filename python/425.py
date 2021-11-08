from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.n = 0
        self.prefix_hash_table = defaultdict(set)
        self.res = []

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.n = len(words[0])
        self.build_prefix_hash_table(words)

        for word in words:
            square = [word]
            self.backtrack(1, square)

        return self.res

    def backtrack(self, step, square):
        if step == self.n:
            self.res.append(square[:])
            return

        prefix = ''.join([word[step] for word in square])

        for candidate in self.get_words_with_prefix(prefix):
            square.append(candidate)
            self.backtrack(step + 1, square)
            square.pop()

    def build_prefix_hash_table(self, words):
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                self.prefix_hash_table[prefix].add(word)

    def get_words_with_prefix(self, prefix):
        if prefix in self.prefix_hash_table:
            return self.prefix_hash_table[prefix]
        return set([])
