class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        res = []

        for i in range(len(text)):
            for word in words:
                j = i + len(word) - 1
                if j < len(text) and text[i:j + 1] == word:
                    res.append([i, j])

        res.sort()

        return res
