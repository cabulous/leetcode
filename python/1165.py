class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        curr_idx = 0
        res = 0

        for ch in word:
            next_idx = keyboard.index(ch)
            res += abs(next_idx - curr_idx)
            curr_idx = next_idx

        return res
