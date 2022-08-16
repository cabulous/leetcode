import re


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = re.compile(r'^(.+)\1+$')
        return pattern.match(s) is not None
