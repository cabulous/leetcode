from typing import List


# https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/99453/Python-Simple-Explanation/103517
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        for word1 in sorted(strs, key=len, reverse=True):
            if sum(self.is_subsequence(word1, word2) for word2 in strs) == 1:
                return len(word1)
        return -1

    def is_subsequence(self, word1, word2):
        word2 = iter(word2)
        return all(c in word2 for c in word1)
