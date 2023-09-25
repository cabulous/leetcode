from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)

        for ch in t:
            if ch not in count or count[ch] == 0:
                return ch
            count[ch] -= 1

        return ''
