import collections


# https://leetcode.com/problems/palindrome-permutation/discuss/69574/1-4-lines-Python-Ruby-C%2B%2B-C-Java
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(v % 2 for v in collections.Counter(s).values()) <= 1
