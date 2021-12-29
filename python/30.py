from collections import Counter, defaultdict
from typing import List


# https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13669/99ms-Python-O(kmn)-Solution
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_counter = Counter(words)
        num_of_words = len(words)
        word_len = len(words[0])
        res = []

        for i in range(word_len):

            left = i
            sub_counter = defaultdict(int)
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):

                word = s[j:j + word_len]

                if word in word_counter:
                    sub_counter[word] += 1
                    count += 1
                    while sub_counter[word] > word_counter[word]:
                        sub_counter[s[left:left + word_len]] -= 1
                        count -= 1
                        left += word_len
                    if count == num_of_words:
                        res.append(left)

                else:
                    left = j + word_len
                    sub_counter = defaultdict(int)
                    count = 0

        return res
