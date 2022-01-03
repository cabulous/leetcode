from typing import List


# https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        letters_count = 0
        cur = []
        res = []

        for word in words:
            if letters_count + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - letters_count):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                letters_count = 0
                cur = []
            letters_count += len(word)
            cur.append(word)

        return res + [' '.join(cur).ljust(maxWidth)]
