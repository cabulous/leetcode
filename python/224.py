# https://leetcode.com/problems/basic-calculator/discuss/62344/Easy-18-lines-C%2B%2B-16-lines-Python
class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        i, signs = 0, [1, 1]

        while i < len(s):
            c = s[i]

            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue

            if c in '+-(':
                if c == '-':
                    sign = -1
                else:
                    sign = 1
                signs.append(signs[-1] * sign)
            elif c == ')':
                signs.pop()

            i += 1

        return total
