class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and self.is_bad(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)

    def is_bad(self, char1, char2):
        return abs(ord(char1) - ord(char2)) == 32
