# https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/363662/Short-python-code-O(n)-time-and-O(1)-space-with-proof-and-visualization
class Solution:
    def lastSubstring(self, s: str) -> str:
        i = 0
        j = 1
        delta = 0

        while j + delta < len(s):
            if s[i + delta] == s[j + delta]:
                delta += 1
                continue
            elif s[i + delta] > s[j + delta]:
                j = j + delta + 1
            else:
                i = max(i + delta + 1, j)
                j = i + 1
            delta = 0

        return s[i:]
