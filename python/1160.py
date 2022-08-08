from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        res = 0

        for word in words:
            word_count = Counter(word)
            if all(word_count[ch] <= chars_count[ch] for ch in word_count):
                res += len(word)

        return res
