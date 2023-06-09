class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if target < letters[0] or letters[-1] <= target:
            return letters[0]

        next_target = chr(ord(target) + 1)
        hi = self.binary_search(letters, next_target)

        return letters[hi]

    def binary_search(self, letters, target):
        lo = 0
        hi = len(letters)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if letters[mi] < target:
                lo = mi + 1
            else:
                hi = mi
        return lo
