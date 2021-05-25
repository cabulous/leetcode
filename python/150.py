from typing import List


# stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        stack = []

        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                operation = operations[token]
                stack.append(operation(num1, num2))
            else:
                stack.append(int(token))

        return stack.pop()


# Reducing the List In-place
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        current_position = 0

        while len(tokens) > 1:
            while tokens[current_position] not in '+-*/':
                current_position += 1

            operator = tokens[current_position]
            num1 = int(tokens[current_position - 2])
            num2 = int(tokens[current_position - 1])

            operation = operations[operator]
            tokens[current_position] = operation(num1, num2)

            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1

        return int(tokens[0])
