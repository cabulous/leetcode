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
                index += 1
                index_start = index
                while index < formula_count and formula[index].isdigit():
                    index += 1
                multiplicity = int(formula[index_start:index] or 1)

                top = stack.pop()
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
        counter = stack.pop()
        for name in sorted(counter):
            if counter[name] > 1:
                res.append(name + str(counter[name]))
            else:
                res.append(name)

        return ''.join(res)
