from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            res = max(res, right - left + 1)
            seen[s[right]] = right

        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = right = 0
        res = 0

        while right < len(s):
            while s[right] in seen:
                seen.discard(s[left])
                left += 1
            res = max(res, right - left + 1)
            seen.add(s[right])
            right += 1

        return res
