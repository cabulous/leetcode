# https://leetcode.com/problems/next-greater-element-iii/discuss/117208/Easy-Python3-beats-100

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(map(int, str(n)))
        i = len(s) - 2
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1
        if i < 0:
            return -1

        j = len(s) - 1
        while j >= 0 and s[j] <= s[i]:
            j -= 1

        s[i], s[j] = s[j], s[i]
        s[i + 1:] = reversed(s[i + 1:])
        res = int(''.join(map(str, s)))

        return res if res <= ((1 << 31) - 1) else -1
