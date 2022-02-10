# https://leetcode.com/problems/detect-capital/discuss/99249/Python-has-useful-methods...
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()
