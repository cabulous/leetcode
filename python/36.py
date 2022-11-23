from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                num = int(num)
                rows[r][num] += 1
                cols[c][num] += 1
                box_idx = (r // 3) * 3 + c // 3
                boxes[box_idx][num] += 1
                if any([rows[r][num] > 1, cols[c][num] > 1, boxes[box_idx][num] > 1]):
                    return False

        return True
