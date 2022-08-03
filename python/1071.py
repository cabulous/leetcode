# https://leetcode.com/problems/greatest-common-divisor-of-strings/discuss/303781/JavaPython-3-3-codes-each%3A-Recursive-iterative-and-regex-w-brief-comments-and-analysis.
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1:
            return str2

        if not str2:
            return str1

        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)

        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)

        return ''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        d = self.gcd(len(str1), len(str2))
        if str1[:d] * (len(str2) // d) == str2 and str2[:d] * (len(str1) // d) == str1:
            return str1[:d]
        return ''

    def gcd(self, a, b):
        return b if a == 0 else self.gcd(b % a, a)
