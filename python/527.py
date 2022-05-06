from collections import defaultdict
from typing import List


# https://leetcode.com/problems/word-abbreviation/discuss/99781/Python-Straightforward-with-Explanation
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        res = [''] * len(words)

        groups = defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        for (size, first_letter, last_letter), enum_words in groups.items():
            enum_words.sort()

            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i > 0:
                    prev_word, _ = enum_words[i - 1]
                    prefix_count = self.longest_common_prefix(word, prev_word)
                    lcp[i] = max(lcp[i], prefix_count)
                    lcp[i - 1] = max(lcp[i - 1], prefix_count)

            for (word, index), prefix_count in zip(enum_words, lcp):
                delta = size - 2 - prefix_count
                if delta <= max(1, len(str(delta)) - 1):
                    res[index] = word
                else:
                    res[index] = word[:prefix_count + 1] + str(delta) + last_letter

        return res

    def longest_common_prefix(self, a, b):
        res = 0
        while res < len(a) and res < len(b) and a[res] == b[res]:
            res += 1
        return res
