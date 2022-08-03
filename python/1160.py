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


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good = []

        for word in words:
            pool = list(chars)
            is_good = True

            for ch in word:
                if ch not in pool:
                    is_good = False
                    break
                pool.remove(ch)

            if is_good:
                good.append(word)

        return sum([len(word) for word in good])
