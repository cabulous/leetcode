from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_lookup = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        stack = []

        for token in tokens:
            if token in operation_lookup:
                num2 = stack.pop()
                num1 = stack.pop()
                operation = operation_lookup[token]
                stack.append(operation(num1, num2))
            else:
                stack.append(int(token))

        return stack.pop()
