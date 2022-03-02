# https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation
class Solution:

    def __init__(self):
        self.string = ''

    def nearestPalindromic(self, n: str) -> str:
        self.string = n
        str_len = len(n)
        candidates = [str(10 ** k + d) for k in (str_len - 1, str_len) for d in (-1, 1)]
        prefix_num = int(n[:(str_len + 1) // 2])

        for prefix_str in map(str, (prefix_num - 1, prefix_num, prefix_num + 1)):
            cand = prefix_str
            if str_len % 2 == 1:
                cand += prefix_str[:-1][::-1]
            else:
                cand += prefix_str[::-1]
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
