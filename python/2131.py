from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        res = 0
        central = False

        for word, word_count in count.items():
            if word == word[::-1]:
                if word_count % 2 == 0:
                    res += word_count
                else:
                    res += word_count - 1
                    central = True
            elif word[0] < word[1]:
                res += 2 * min(word_count, count[word[::-1]])

        if central:
            res += 1

        return 2 * res


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        alphabet_size = 26
        count = [[0] * alphabet_size for _ in range(alphabet_size)]

        for word in words:
            count[ord(word[0]) - ord('a')][ord(word[1]) - ord('a')] += 1

        res = 0
        central = False

        for i in range(alphabet_size):
            if count[i][i] % 2 == 0:
                res += count[i][i]
            else:
                res += count[i][i] - 1
                central = True
            for j in range(i + 1, alphabet_size):
                res += 2 * min(count[i][j], count[j][i])

        if central:
            res += 1

        return 2 * res
