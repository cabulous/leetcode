from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        t_counts = Counter(t)
        window_counts = Counter()
        required = len(t_counts)
        formed = 0
        left, right = 0, 0
        res = float('inf'), 0, 0

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            if window_counts[char] == t_counts[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < res[0]:
                    res = right - left + 1, left, right
                char_left = s[left]
                window_counts[char_left] -= 1
                if window_counts[char_left] < t_counts[char_left]:
                    formed -= 1
                left += 1

            right += 1

        win_size, win_left, win_right = res
        if win_size == float('inf'):
            return ''

        return s[win_left:win_right + 1]
