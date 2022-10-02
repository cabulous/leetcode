from typing import List


# https://leetcode.com/problems/lonely-pixel-i/discuss/790470/Python3-3-lines-Lonely-Pixel-I
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = [sum(cell == 'B' for cell in row) for row in picture]
        cols = [sum(cell == 'B' for cell in col) for col in zip(*picture)]
        return sum(
            picture[r][c] == 'B' and rows[r] == cols[c] == 1
            for r in range(len(picture))
            for c in range(len(picture[r]))
        )
