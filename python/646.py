class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        prev = float('-inf')
        res = 0
        for n1, n2 in sorted(pairs, key=lambda x: x[1]):
            if prev < n1:
                prev = n2
                res += 1
        return res
