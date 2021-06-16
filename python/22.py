class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if not n:
            return ['']

        res = []

        def helper(s='', left=0, right=0):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                helper(s + '(', left + 1, right)
            if right < left:
                helper(s + ')', left, right + 1)

        helper()

        return res


# Closure Number
class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if not n:
            return ['']

        res = []

        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - c - 1):
                    res.append('({}){}'.format(left, right))

        return res
