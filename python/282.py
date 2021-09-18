from typing import List


# https://leetcode.com/problems/expression-add-operators/discuss/71968/Clean-Python-DFS-with-comments
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        def backtrack(idx=0, path='', value=0, prev=None):
            if idx == len(num) and value == target:
                ans.append(path)
                return

            for i in range(idx + 1, len(num) + 1):
                if i == idx + 1 or (i > idx + 1 and num[idx] != '0'):
                    curr = int(num[idx:i])
                    if prev is None:
                        backtrack(i, num[idx:i], curr, curr)
                    else:
                        backtrack(i, path + '+' + num[idx:i], value + curr, curr)
                        backtrack(i, path + '-' + num[idx:i], value - curr, -curr)
                        backtrack(i, path + '*' + num[idx:i], value - prev + prev * curr, prev * curr)

        backtrack()
        return ans


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(index, pre_operand, cur_operand, value, string):
            if index == n:
                if value == target and cur_operand == 0:
                    ans.append(''.join(string[1:]))
                return

            cur_operand = cur_operand * 10 + int(num[index])
            str_op = str(cur_operand)

            if cur_operand > 0:
                backtrack(index + 1, pre_operand, cur_operand, value, string)

            string.append('+')
            string.append(str_op)
            backtrack(index + 1, cur_operand, 0, value + cur_operand, string)
            string.pop()
            string.pop()

            if string:
                string.append('-')
                string.append(str_op)
                backtrack(index + 1, -cur_operand, 0, value - cur_operand, string)
                string.pop()
                string.pop()

                string.append('*')
                string.append(str_op)
                backtrack(index + 1, cur_operand * pre_operand, 0, value - pre_operand + (cur_operand * pre_operand),
                          string)
                string.pop()
                string.pop()

        backtrack(0, 0, 0, 0, [])
        return ans
