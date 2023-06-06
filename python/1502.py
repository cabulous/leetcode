class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        gap = (max(arr) - min(arr)) / (len(arr) - 1)
        if gap == 0:
            return True
        s = set(num - min(arr) for num in arr)
        return len(s) == len(arr) and all(diff % gap == 0 for diff in s)
