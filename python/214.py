# https://leetcode.com/problems/shortest-palindrome/discuss/60099/AC-in-288-ms-simple-brute-force
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_s = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(reversed_s[i:]):
                return reversed_s[:i] + s
