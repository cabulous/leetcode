from typing import List


# https://leetcode.com/problems/concatenated-words/discuss/159348/Python-DFS-readable-solution
class Solution:

    def __init__(self):
        self.memo = {}
        self.words = {}

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.words = set(words)
        return [word for word in self.words if self.dfs(word)]

    def dfs(self, word):
        if word in self.memo:
            return self.memo[word]

        for end_index in range(1, len(word)):
            prefix, suffix = word[:end_index], word[end_index:]

            if prefix in self.words and suffix in self.words:
                self.memo[word] = True
                return True

            if prefix in self.words and self.dfs(suffix):
                self.memo[word] = True
                return True

        self.memo[word] = False
        return False
