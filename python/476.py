from math import floor, log2


class Solution:
    def findComplement(self, num: int) -> int:
        todo, bit = num, 1
        while todo:
            num ^= bit
            bit <<= 1
            todo >>= 1
        return num


class Solution:
    def findComplement(self, num: int) -> int:
        n = floor(log2(num)) + 1
        bitmask = (1 << n) - 1
        return bitmask ^ num


class Solution:
    def findComplement(self, num: int) -> int:
        return (1 << num.bit_length()) - 1 - num
