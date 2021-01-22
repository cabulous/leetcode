from collections import Counter


# https://leetcode.com/problems/determine-if-two-strings-are-close/discuss/1029064/Python-Oneliner-with-Counter-explained
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
