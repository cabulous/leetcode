# https://leetcode.com/problems/push-dominoes/discuss/132332/JavaC%2B%2BPython-Two-Pointers
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        res = ''
        i = 0

        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue

            if i > 0:
                res += dominoes[i]

            middle = j - i - 1

            if dominoes[i] == dominoes[j]:
                res += dominoes[i] * middle
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                res += '.' * middle
            else:
                res += 'R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2)

            i = j

        return res
