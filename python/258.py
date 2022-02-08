class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
