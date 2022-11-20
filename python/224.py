# https://leetcode.com/problems/basic-calculator/solutions/2831471/python3-stack-approach-with-detailed-explanations-o-n/
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        stack = [0]

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == ' ':
                continue
            elif ch == '+':
                stack[-1] += num * sign
                sign = 1
                num = 0
            elif ch == '-':
                stack[-1] += num * sign
                sign = -1
                num = 0
            elif ch == '(':
                stack.extend([sign, 0])
                sign = 1
                num = 0
            elif ch == ')':
                last_num = (stack.pop() + num * sign) * stack.pop()
                stack[-1] += last_num
                sign = 1
                num = 0

        return stack[-1] + num * sign
