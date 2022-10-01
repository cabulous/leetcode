from typing import List


# https://leetcode.com/problems/lonely-pixel-i/discuss/790470/Python3-3-lines-Lonely-Pixel-I
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = [sum(col == 'B' for col in row) for row in picture]
        cols = [sum(row == 'B' for row in col) for col in zip(*picture)]
        return sum(
            picture[r][c] == 'B' and rows[r] == 1 and cols[c] == 1
            for r in range(len(picture))
            for c in range(len(picture[r]))
        )
