from typing import List
from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_count = Counter(self.bitmask(word) for word in words)
        res = []

        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            count = word_count[first]
            mask = self.bitmask(puzzle[1:])
            sub_mask = mask
            while sub_mask:
                count += word_count[sub_mask | first]
                sub_mask = (sub_mask - 1) & mask
            res.append(count)

        return res

    def bitmask(self, word):
        mask = 0
        for letter in word:
            mask |= 1 << (ord(letter) - ord('a'))
        return mask
