from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s) * k == 0:
            return 0

        distinct_char = Counter()
        left = 0
        res = 0

        for right in range(len(s)):
            distinct_char[s[right]] += 1
            while len(distinct_char) > k:
                distinct_char[s[left]] -= 1
                if distinct_char[s[left]] == 0:
                    distinct_char.pop(s[left])
                left += 1
            res = max(res, right - left + 1)

        return res
