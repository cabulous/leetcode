from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula_count = len(formula)
        stack = [Counter()]
        index = 0

        while index < formula_count:
            if formula[index] == '(':
                stack.append(Counter())
                index += 1
            elif formula[index] == ')':
                top = stack.pop()
                index += 1
                index_start = index
                while index < formula_count and formula[index].isdigit():
                    index += 1
                multiplicity = int(formula[index_start:index] or 1)
                for name, count in top.items():
                    stack[-1][name] += count * multiplicity
            else:
                index_start = index
                index += 1
                while index < formula_count and formula[index].islower():
                    index += 1
                name = formula[index_start:index]

                index_start = index
                while index < formula_count and formula[index].isdigit():
                    index += 1
                multiplicity = int(formula[index_start:index] or 1)
                stack[-1][name] += multiplicity

        res = []
        for name in sorted(stack[-1]):
            if stack[-1][name] > 1:
                res.append(name + str(stack[-1][name]))
            else:
                res.append(name)

        return ''.join(res)
