from collections import Counter
from typing import List


# https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13669/99ms-Python-O(kmn)-Solution
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        target_word_count = len(words)
        word_count = Counter(words)
        res = []

        for i in range(word_len):
            left = i
            curr_count = Counter()
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_count:
                    curr_count[word] += 1
                    count += 1
                    while curr_count[word] > word_count[word]:
                        curr_count[s[left:left + word_len]] -= 1
                        count -= 1
                        left += word_len
                    if count == target_word_count:
                        res.append(left)

                else:
                    left = j + word_len
                    curr_count = Counter()
                    count = 0

        return res
