# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/discuss/944594/JavaPython-3-O(n)-and-O(1)-codes-w-brief-explanation-and-analysis.

# greedily reversely place values
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res, i = ['a'] * n, n - 1
        k -= n
        while i >= 0 and k > 0:
            res[i] = chr(ord(res[i]) + min(k, 25))
            k -= min(k, 25)
            i -= 1
        return ''.join(res)


# math
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z, r = divmod(k - n - 1, 25)
        a = n - z - 1
        return 'a' * a + chr(r + 1 + ord('a')) + 'z' * z
