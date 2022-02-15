# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/discuss/322928/JavaC%2B%2BPython-Sliding-Window
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        cur = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in cur:
                cur.remove(s[left])
                left += 1
            cur.add(s[right])
            res += right - left + 1 >= k

        return res
