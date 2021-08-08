# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/211940/Python-7-lines-with-some-explanations-and-thoughts
class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0

        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        cut = [-1] + [i for i in range(len(s))]

        for i in range(len(s) * 2 - 1):
            left = i // 2
            right = i - left
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cut[right + 1] = min(cut[right + 1], cut[left] + 1)
                left -= 1
                right += 1

        return cut[-1]


# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42205/56-ms-python-with-explanation
class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0

        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        cut = [-1] + [x for x in range(len(s))]

        for i in range(len(s)):
            odd_r, even_r = 0, 0
            while i - odd_r >= 0 and i + odd_r < len(s) and s[i - odd_r] == s[i + odd_r]:
                cut[i + odd_r + 1] = min(cut[i + odd_r + 1], cut[i - odd_r] + 1)
                odd_r += 1
            while i - even_r >= 0 and i + even_r + 1 < len(s) and s[i - even_r] == s[i + even_r + 1]:
                cut[i + even_r + 2] = min(cut[i + even_r + 2], cut[i - even_r] + 1)
                even_r += 1

        return cut[-1]
