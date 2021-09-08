from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = []
        shift_dist = sum(shifts) % 26
        for i, c in enumerate(s):
            cur_dist = ord(c) - ord('a')
            new_c = chr(ord('a') + (cur_dist + shift_dist) % 26)
            ans.append(new_c)
            shift_dist = (shift_dist - shifts[i]) % 26
        return ''.join(ans)
