from collections import Counter


# https://leetcode.com/problems/reordered-power-of-2/discuss/149843/C%2B%2BJavaPython-Straight-Forward
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return sorted(str(N)) in [sorted(str(1 << i)) for i in range(30)]


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        c = Counter(str(N))
        return any(c == Counter(str(1 << i)) for i in range(30))
