from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique_chars = ['']
        res = 0

        for word in arr:
            for unique in unique_chars:
                new_word = unique + word
                if len(new_word) == len(set(new_word)):
                    unique_chars.append(new_word)
                    res = max(res, len(new_word))

        return res
