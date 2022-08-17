from typing import List

MORSE_CODE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        for word in words:
            curr = []
            for ch in word:
                curr.append(MORSE_CODE[ord(ch) - ord('a')])
            res.add(''.join(curr))
        return len(res)
