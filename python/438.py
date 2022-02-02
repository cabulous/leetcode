from collections import Counter
from typing import List


# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []

        s_count = Counter(s[:p_len - 1])
        p_count = Counter(p)
        res = []

        for i in range(p_len - 1, s_len):
            s_count[s[i]] += 1
            start_index = i - p_len + 1

            if s_count == p_count:
                res.append(start_index)

            s_count[s[start_index]] -= 1
            if s_count[s[start_index]] == 0:
                del s_count[s[start_index]]

        return res
