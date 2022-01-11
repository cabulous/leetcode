from collections import defaultdict
from typing import List


class Solution:

    def __init__(self):
        self.memo = defaultdict(list)
        self.word_set = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.word_set = set(wordDict)
        self.helper(s)
        return [' '.join(words) for words in self.memo[s]]

    def helper(self, s):
        if not s:
            return [[]]

        if s in self.memo:
            return self.memo[s]

        for end_index in range(1, len(s) + 1):
            word = s[:end_index]
            if word in self.word_set:
                for sub_sentence in self.helper(s[end_index:]):
                    self.memo[s].append([word] + sub_sentence)

        return self.memo[s]
