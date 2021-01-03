class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if not n:
            return ['']

        ans = []

        def helper(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                helper(s + '(', left + 1, right)
            if right < left:
                helper(s + ')', left, right + 1)

        helper()
        return ans


# Closure Number
class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if not n:
            return ['']

        ans = []

        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - c - 1):
                    ans.append('({}){}'.format(left, right))

        return ans
