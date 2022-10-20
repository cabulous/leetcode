from functools import lru_cache


# https://leetcode.com/problems/string-compression-ii/discuss/755970/Python-dynamic-programming
class Solution:

    def __init__(self):
        self.s = ''
        self.s_len = 0

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.s = s
        self.s_len = len(s)
        return self.count(0, '', 0, k)

    @lru_cache(None)
    def count(self, curr_idx, last_char, last_char_count, quota):
        if quota < 0:
            return float('inf')

        if self.s_len <= curr_idx:
            return 0

        if self.s[curr_idx] == last_char:
            inr = 1 if last_char_count in (1, 9, 99) else 0
            return inr + self.count(curr_idx + 1, last_char, last_char_count + 1, quota)

        keep_count = 1 + self.count(curr_idx + 1, self.s[curr_idx], 1, quota)
        del_count = self.count(curr_idx + 1, last_char, last_char_count, quota - 1)

        return min(keep_count, del_count)
