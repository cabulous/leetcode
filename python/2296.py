# https://leetcode.com/problems/design-a-text-editor/discuss/2112018/Python-Simple-Solution
class TextEditor:

    def __init__(self):
        self.s = ''
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.s = self.s[:self.cursor] + text + self.s[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        next_cursor = max(0, self.cursor - k)
        self.s = self.s[:next_cursor] + self.s[self.cursor:]
        res = self.cursor - next_cursor
        self.cursor = next_cursor
        return res

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        start = max(0, self.cursor - 10)
        return self.s[start:self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.s), self.cursor + k)
        start = max(0, self.cursor - 10)
        return self.s[start:self.cursor]
