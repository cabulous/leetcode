# https://leetcode.com/problems/break-a-palindrome/discuss/489774/JavaC%2B%2BPython-Easy-and-Concise
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ''

        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]

        return palindrome[:-1] + 'b'
