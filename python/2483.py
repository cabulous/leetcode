class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr = 0
        best = 0
        res = -1

        for i, c in enumerate(customers):
            curr += 1 if c == 'Y' else -1
            if curr > best:
                best = curr
                res = i

        return res
