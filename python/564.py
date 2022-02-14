# https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation
class Solution:

    def __init__(self):
        self.string = ''

    def nearestPalindromic(self, n: str) -> str:
        self.string = n
        str_len = len(n)
        candidates = [str(10 ** k + d) for k in (str_len - 1, str_len) for d in (-1, 1)]
        prefix = int(n[:(str_len + 1) // 2])

        for start in map(str, (prefix - 1, prefix, prefix + 1)):
            cand = start
            if str_len % 2 == 1:
                cand += start[:-1][::-1]
            else:
                cand += start[::-1]
            candidates.append(cand)

        res = None

        for cand in candidates:
            if cand != n:
                if res is None:
                    res = cand
                elif self.delta(cand) < self.delta(res):
                    res = cand
                elif self.delta(cand) == self.delta(res) and int(cand) < int(res):
                    res = cand

        return res

    def delta(self, a_str):
        return abs(int(self.string) - int(a_str))
