class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        for row in range(len(words)):
            col_vals = []
            for col in range(len(words)):
                if row < len(words[col]):
                    col_vals.append(words[col][row])
            if words[row] != ''.join(col_vals):
                return False
        return True
