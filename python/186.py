from typing import List


# https://leetcode.com/problems/reverse-words-in-a-string-ii/discuss/53832/Python-solution
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        self.reverse(s, 0, len(s) - 1)

        begin = 0

        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, begin, i - 1)
                begin = i + 1
            elif i == len(s) - 1:
                self.reverse(s, begin, i)

    def reverse(self, string, left, right):
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
