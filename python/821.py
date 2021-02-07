from typing import List


# https://leetcode.com/problems/shortest-distance-to-a-character/discuss/125788/C%2B%2BJavaPython-2-Pass-with-Explanation
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0 if x == c else n for x in s]
        for i in range(1, n):
            ans[i] = min(ans[i], ans[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            ans[i] = min(ans[i], ans[i + 1] + 1)
        return ans


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev = float('-inf')
        ans = []

        for i, x in enumerate(s):
            if x == c:
                prev = i
            ans.append(i - prev)

        prev = float('inf')

        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
