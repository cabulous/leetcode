# https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        count = 0
        curr = []
        res = []

        for word in words:
            if count + len(curr) + len(word) > maxWidth:
                for i in range(maxWidth - count):
                    curr[i % (len(curr) - 1 or 1)] += ' '
                res.append(''.join(curr))
                count = 0
                curr = []
            count += len(word)
            curr.append(word)

        return res + [' '.join(curr).ljust(maxWidth)]
