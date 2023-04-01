class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        same = word1 == word2
        idx1 = -1
        idx2 = -1
        res = len(wordsDict)

        for i, word in enumerate(wordsDict):
            if word == word1:
                idx1 = i
                if idx2 != -1:
                    res = min(res, abs(idx1 - idx2))
            if word == word2:
                idx2 = i
                if idx1 != -1 and not same:
                    res = min(res, abs(idx1 - idx2))

        return res
