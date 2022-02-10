from functools import lru_cache


# https://leetcode.com/problems/string-compression-ii/discuss/755970/Python-dynamic-programming
class Solution:

    def __init__(self):
        self.s_len = 0
        self.s = ''

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.s_len = len(s)
        self.s = s

        return self.count(0, '', 0, k)

    @lru_cache(None)
    def count(self, curr_index, last_char, last_char_count, quota):
        if quota < 0:
            return float('inf')

        if self.s_len <= curr_index:
            return 0

        if self.s[curr_index] == last_char:
            incr = 1 if last_char_count in (1, 9, 99) else 0
            return incr + self.count(curr_index + 1, last_char, last_char_count + 1, quota)

        keep_count = 1 + self.count(curr_index + 1, self.s[curr_index], 1, quota)
        del_count = self.count(curr_index + 1, last_char, last_char_count, quota - 1)

        return min(keep_count, del_count)
