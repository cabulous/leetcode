from collections import Counter
from typing import List


# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        s_count = Counter(s[:len(p) - 1])
        p_count = Counter(p)
        left = 0
        res = []

        for right in range(len(p) - 1, len(s)):
            s_count[s[right]] += 1

            if s_count == p_count:
                res.append(left)

            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]

            left += 1

        return res
