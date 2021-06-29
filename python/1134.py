import math


class Solution:
    def isArmstrong(self, n: int) -> bool:
        total = 0
        k = math.floor(math.log10(n)) + 1
        num = n
        while num > 0:
            num, digit = divmod(num, 10)
            total += digit ** k
        return total == n


class Solution:
    def isArmstrong(self, n: int) -> bool:
        num_string = str(n)
        num_len = len(num_string)
        total = 0
        for num in num_string:
            total += int(num) ** num_len
        return total == n
