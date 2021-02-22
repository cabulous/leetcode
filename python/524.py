from typing import List


# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99590/Short-Python-solutions
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def is_subsequence(x):
            it = iter(s)
            return all(c in it for c in x)

        return max(sorted(filter(is_subsequence, d)) + [''], key=len)
