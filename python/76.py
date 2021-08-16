import math
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        dict_t = Counter(t)
        window_counts = {}
        required = len(dict_t)
        formed = 0
        left, right = 0, 0
        ans = math.inf, 0, 0

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            while left <= right and formed == required:
                if right - left + 1 < ans[0]:
                    ans = ((right - left + 1), left, right)
                char = s[left]
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                left += 1
            right += 1

        return '' if ans[0] == math.inf else s[ans[1]:ans[2] + 1]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        dict_t = Counter(t)
        required = len(dict_t)
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        left, right = 0, 0
        formed = 0
        window_counts = {}
        ans = math.inf, None, None

        while right < len(filtered_s):
            char = filtered_s[right][1]
            window_counts[char] = window_counts.get(char, 0) + 1
            if window_counts[char] == dict_t[char]:
                formed += 1
            while left <= right and formed == required:
                char = filtered_s[left][1]
                start = filtered_s[left][0]
                end = filtered_s[right][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                window_counts[char] -= 1
                if window_counts[char] < dict_t[char]:
                    formed -= 1
                left += 1
            right += 1

        return '' if ans[0] == math.inf else s[ans[1]:ans[2] + 1]
