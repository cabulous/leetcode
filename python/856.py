# Count Cores
# O(N), O(1)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = balance = 0
        for i, x in enumerate(S):
            if x == '(':
                balance += 1
            else:
                balance -= 1
                if S[i - 1] == '(':
                    ans += (1 << balance)
        return ans


# stack
# O(N), O(N)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack.pop()
