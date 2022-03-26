from typing import List


# https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC%2B%2BPython-DP-using-Map-or-Stack
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher = [0] * n
        next_lower = [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher = [0] * n
        lower = [0] * n
        higher[-1] = lower[-1] = 1
        for i in reversed(range(n - 1)):
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]

        return sum(higher)
