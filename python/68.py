from typing import List


# https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        letters_count = 0
        curr_line = []
        res = []

        for word in words:
            if letters_count + len(word) + len(curr_line) > maxWidth:
                for i in range(maxWidth - letters_count):
                    curr_line[i % (len(curr_line) - 1 or 1)] += ' '
                res.append(''.join(curr_line))
                letters_count = 0
                curr_line = []
            letters_count += len(word)
            curr_line.append(word)

        return res + [' '.join(curr_line).ljust(maxWidth)]
