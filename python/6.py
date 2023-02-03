import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        sections = math.ceil(len(s) / (2 * numRows - 2.0))
        cols = sections * (numRows - 1)
        matrix = [[''] * cols for _ in range(numRows)]

        curr_row = 0
        curr_col = 0
        curr_str_idx = 0

        while curr_str_idx < len(s):
            while curr_row < numRows and curr_str_idx < len(s):
                matrix[curr_row][curr_col] = s[curr_str_idx]
                curr_row += 1
                curr_str_idx += 1

            curr_row -= 2
            curr_col += 1

            while curr_row > 0 and curr_col < cols and curr_str_idx < len(s):
                matrix[curr_row][curr_col] = s[curr_str_idx]
                curr_row -= 1
                curr_col += 1
                curr_str_idx += 1

        res = [c for r in matrix for c in r]

        return ''.join(res)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = []
        chars_in_section = 2 * (numRows - 1)

        for curr_row in range(numRows):
            idx = curr_row
            while idx < len(s):
                res.append(s[idx])
                if curr_row not in (0, numRows - 1):
                    chars_in_between = chars_in_section - 2 * curr_row
                    next_idx = idx + chars_in_between
                    if next_idx < len(s):
                        res.append(s[next_idx])
                idx += chars_in_section

        return ''.join(res)
