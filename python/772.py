class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        nums, ops = [], []
        i = 0

        while i < len(s):
            c = s[i]
            if c == ' ':
                i += 1
                continue
            elif c.isdigit():
                num = int(c)
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                nums.append(num)
            elif c == '(':
                ops.append(c)
            elif c == ')':
                while ops[-1] != '(':
                    nums.append(self.operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()
            elif c in '+-*/':
                while len(ops) > 0 and self.precedence(c, ops[-1]):
                    nums.append(self.operation(ops.pop(), nums.pop(), nums.pop()))
                ops.append(c)
            i += 1

        while len(ops) > 0:
            nums.append(self.operation(ops.pop(), nums.pop(), nums.pop()))

        return nums[-1]

    def operation(self, op, second, first):
        if op == '+':
            return first + second
        if op == '-':
            return first - second
        if op == '*':
            return first * second
        if op == '/':
            return first // second

    def precedence(self, curr_op, op_from_ops):
        if op_from_ops in '()':
            return False
        if curr_op in '*/' and op_from_ops in '+-':
            return False
        return True
