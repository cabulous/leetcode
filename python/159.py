from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        left = 0
        right = 0
        right_most = defaultdict(int)
        res = 2

        while right < len(s):
            right_most[s[right]] = right
            right += 1

            if len(right_most) == 3:
                del_idx = min(right_most.values())
                del right_most[s[del_idx]]
                left = del_idx + 1

            res = max(res, right - left)

        return res
