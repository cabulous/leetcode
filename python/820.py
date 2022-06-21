from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)

        for word in set(words):
            for i in range(1, len(word)):
                good.discard(word[i:])

        return sum(len(w) + 1 for w in good)
