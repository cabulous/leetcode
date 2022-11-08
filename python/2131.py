from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        central = False
        res = 0

        for word, word_count in count.items():
            if word[0] == word[1]:
                if word_count % 2 == 0:
                    res += word_count
                else:
                    res += word_count - 1
                    central = True
            elif word[0] < word[1]:
                res += min(word_count, count[word[::-1]]) * 2

        if central:
            res += 1

        return 2 * res
