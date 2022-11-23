from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    num = int(num)
                    box_idx = (r // 3) * 3 + c // 3
                    boxes[box_idx][num] += 1
                    rows[r][num] += 1
                    cols[c][num] += 1
                    if rows[r][num] > 1 or cols[c][num] > 1 or boxes[box_idx][num] > 1:
                        return False

        return True
