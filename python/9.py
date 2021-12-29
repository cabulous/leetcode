class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs = str(x)
        return xs == xs[::-1]
