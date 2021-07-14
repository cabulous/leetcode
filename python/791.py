from collections import Counter


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        count = Counter(str)
        res = []

        for c in order:
            res.append(c * count[c])
            count[c] = 0

        for c in count:
            res.append(c * count[c])

        return ''.join(res)
