# https://leetcode.com/problems/decode-ways-ii/discuss/105262/Python-6-lines-DP-solution
class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7
        one = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
        two = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1,
               '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2,
               '*5': 2, '*6': 2, '*7': 1, '*8': 1, '*9': 1, '1*': 9, '2*': 6, '**': 15}

        prev = 1
        curr = one.get(s[0], 0)

        for i in range(1, len(s)):
            prev, curr = curr, (one.get(s[i], 0) * curr + two.get(s[i - 1:i + 1], 0) * prev) % mod

        return curr
