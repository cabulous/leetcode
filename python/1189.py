from collections import Counter


# https://leetcode.com/problems/maximum-number-of-balloons/discuss/382396/JavaPython-3-Count-solution-w-analysis.
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        cnt_balloon = Counter('balloon')
        return min(cnt[c] // cnt_balloon[c] for c in cnt_balloon)
