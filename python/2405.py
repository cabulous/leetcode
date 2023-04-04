class Solution:
    def partitionString(self, s: str) -> int:
        seen = {}
        res = 1

        for ch in s:
            if ch in seen:
                res += 1
                seen.clear()
            seen[ch] = True

        return res
