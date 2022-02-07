from collections import deque
from typing import List


# https://leetcode.com/problems/sliding-puzzle/discuss/113620/JavaPython-3-BFS-clean-codes-w-comment-Time-and-space%3A-O(m-*-n-*-(m-*-n)!).
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        curr_s = ''.join(str(digit) for row in board for digit in row)
        queue = deque([(curr_s, curr_s.index('0'))])
        seen = {curr_s}
        height, width = len(board), len(board[0])
        steps = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            for _ in range(len(queue)):
                curr_s, zero_idx = queue.popleft()

                if curr_s == '123450':
                    return steps

                zero_row_idx = zero_idx // width
                zero_col_idx = zero_idx % width

                for dr, dc in directions:
                    nr, nc = zero_row_idx + dr, zero_col_idx + dc

                    if 0 <= nr < height and 0 <= nc < width:
                        curr_board = [digit for digit in curr_s]
                        next_zero_idx = nr * width + nc
                        curr_board[zero_idx], curr_board[next_zero_idx] = curr_board[next_zero_idx], '0'
                        next_s = ''.join(curr_board)

                        if next_s not in seen:
                            seen.add(next_s)
                            queue.append((next_s, next_zero_idx))

            steps += 1

        return -1
