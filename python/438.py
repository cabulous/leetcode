from collections import Counter
from typing import List


# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        win_count = Counter(s[:len(p)])
        p_count = Counter(p)

        win_size = len(p)
        res = []

        for right in range(len(p), len(s)):
            left = right - win_size

            if win_count == p_count:
                res.append(left)

            win_count[s[right]] += 1

            win_count[s[left]] -= 1
            if win_count[s[left]] == 0:
                del win_count[s[left]]

        if win_count == p_count:
            res.append(len(s) - win_size)

        return res
