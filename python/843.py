from collections import Counter
import random
from typing import List


class Master:
    def guess(self, word: str) -> int:
        pass


# https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        n = 0
        while n < 6:
            count = [Counter(w[i] for w in wordlist) for i in range(6)]
            guess = max(wordlist, key=lambda w: sum(count[i][c] for i, c in enumerate(w)))
            n = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]

    def match(self, w1, w2):
        return sum(i == j for i, j in zip(w1, w2))


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        random.shuffle(wordlist)
        for _ in range(10):
            guess = random.choice(wordlist)
            n = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]

    def match(self, w1, w2):
        return sum(i == j for i, j in zip(w1, w2))
