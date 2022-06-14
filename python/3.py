from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        left = 0
        res = 0

        for right, ch in enumerate(s):
            if ch in seen:
                left = max(left, seen[ch] + 1)
            res = max(res, right - left + 1)
            seen[ch] = right

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
