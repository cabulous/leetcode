from typing import List


# https://leetcode.com/problems/find-and-replace-pattern/discuss/161288/C%2B%2BJavaPython-Normalise-Word
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [w for w in words if self.hash_pattern(w) == self.hash_pattern(pattern)]

    def hash_pattern(self, word):
        m = {}
        return [m.setdefault(ch, len(m)) for ch in word]
