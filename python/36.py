from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == '.':
                    continue
                rows[r][val] += 1
                cols[c][val] += 1
                box_idx = r // 3 * 3 + c // 3
                boxes[box_idx][val] += 1
                if any([rows[r][val] > 1, cols[c][val] > 1, boxes[box_idx][val] > 1]):
                    return False

        return True
