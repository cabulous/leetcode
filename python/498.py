from collections import defaultdict


# Diagonal Iteration and Reversal
class Solution:
    def findDiagonalOrder(self, matrix: [[int]]) -> [int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        res = []
        intermediate = []

        for d in range(n + m - 1):
            intermediate.clear()
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            while r < m and c >= 0:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                res.extend(intermediate[::-1])
            else:
                res.extend(intermediate)

        return res


class Solution:
    def findDiagonalOrder(self, matrix: [[int]]) -> [int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        d = defaultdict(list)
        ans = []

        for i in range(m):
            for j in range(n):
                d[i + j].append(matrix[i][j])

        for entry in d.items():
            if entry[0] % 2 == 0:
                ans += entry[1][::-1]
            else:
                ans += entry[1]

        return ans
