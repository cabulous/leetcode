from collections import defaultdict
from string import ascii_lowercase
from typing import List


class Solution:

    def __init__(self):
        self.word_set = set()

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.word_set = set(wordList)
        self.word_set.discard(beginWord)

        level = {beginWord: [[beginWord]]}
        while level:
            next_level = defaultdict(list)
            for word, paths in level.items():
                if word == endWord:
                    return paths
                for nei in self.neighbors(word):
                    for path in paths:
                        next_level[nei].append(path + [nei])
            self.word_set -= set(next_level.keys())
            level = next_level

        return []

    def neighbors(self, word):
        for i in range(len(word)):
            for ch in ascii_lowercase:
                next_word = word[:i] + ch + word[i + 1:]
                if next_word in self.word_set:
                    yield next_word
