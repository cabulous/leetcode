from collections import defaultdict


# https://leetcode.com/problems/total-appeal-of-a-string/discuss/1996390/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation
class Solution:
    def appealSum(self, s: str) -> int:
        last = defaultdict(lambda: -1)
        res = 0

        for index, ch in enumerate(s):
            res += (index - last[ch]) * (len(s) - index)
            last[ch] = index

        return res
