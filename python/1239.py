from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = ['']
        best = 0

        for word in arr:
            for i in range(len(res)):
                new_word = res[i] + word
                if len(new_word) != len(set(new_word)):
                    continue
                res.append(new_word)
                best = max(best, len(new_word))

        return best
