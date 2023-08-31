class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        prev_end = float('-inf')
        res = 0
        for start, end in sorted(pairs, key=lambda x: x[1]):
            if prev_end < start:
                prev_end = end
                res += 1
        return res
