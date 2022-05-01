class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.get_res(s) == self.get_res(t)

    def get_res(self, s):
        stack = []
        for ch in s:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
