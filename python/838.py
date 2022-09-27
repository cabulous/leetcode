# https://leetcode.com/problems/push-dominoes/discuss/132332/JavaC%2B%2BPython-Two-Pointers
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        res = ''
        left = 0

        for right in range(1, len(dominoes)):
            if dominoes[right] == '.':
                continue

            if left > 0:
                res += dominoes[left]

            between = right - left - 1

            if dominoes[left] == dominoes[right]:
                res += dominoes[left] * between
            elif dominoes[left] == 'L' and dominoes[right] == 'R':
                res += '.' * between
            else:
                res += 'R' * (between // 2) + '.' * (between % 2) + 'L' * (between // 2)

            left = right

        return res
