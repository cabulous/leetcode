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
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i + j not in d:
                    d[i + j] = [matrix[i][j]]
                else:
                    d[i + j].append(matrix[i][j])

        ans = []
        for entry in d.items():
            if entry[0] % 2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]

        return ans