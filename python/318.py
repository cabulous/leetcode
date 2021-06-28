from typing import List
from collections import defaultdict


#  Bitmasks + Precomputation + Hashmap
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        hashmap = defaultdict(int)
        bit_number = lambda x: ord(x) - ord('a')

        for word in words:
            bitmask = 0
            for ch in word:
                bitmask |= 1 << bit_number(ch)
            hashmap[bitmask] = max(hashmap[bitmask], len(word))

        max_val = 0

        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    max_val = max(max_val, hashmap[x] * hashmap[y])

        return max_val


# Bitmasks + Precomputation
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n
        bit_number = lambda ch: ord(ch) - ord('a')

        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                bitmask |= 1 << bit_number(ch)
            masks[i] = bitmask
            lens[i] = len(words[i])

        max_val = 0

        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    max_val = max(max_val, lens[i] * lens[j])

        return max_val
