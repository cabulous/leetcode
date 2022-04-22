class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                delete_left = s[left + 1:right + 1]
                delete_right = s[left:right]
                return self.is_palindrome(delete_left) or self.is_palindrome(delete_right)
            left += 1
            right -= 1

        return True

    def is_palindrome(self, s):
        return s == s[::-1]
