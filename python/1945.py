class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        res = 0

        for _ in range(k):
            res = sum(int(d) for d in s)
            s = str(res)

        return res
