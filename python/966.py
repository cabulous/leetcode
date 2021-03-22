import re
from typing import List


# https://leetcode.com/problems/vowel-spellchecker/discuss/211189/JavaC%2B%2BPython-Two-HashMap
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = {w: w for w in wordlist}
        cap = {w.lower(): w for w in wordlist[::-1]}
        vowel = {re.sub('[aeiou]', '#', w.lower()): w for w in wordlist[::-1]}
        return [words.get(w) or cap.get(w.lower()) or vowel.get(re.sub('[aeiou]', '#', w.lower()), '') for w in queries]


class Solution:
    def __init__(self):
        self.words_unique = set()
        self.words_cap = {}
        self.words_vowel = {}

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        self.words_unique = set(wordlist)

        for w in wordlist:
            word_lower = w.lower()
            self.words_cap.setdefault(word_lower, w)
            self.words_vowel.setdefault(self.devowel(word_lower), w)

        return map(self.solve, queries)

    def devowel(self, word):
        return ''.join('*' if c in 'aeiou' else c for c in word)

    def solve(self, query):
        if query in self.words_unique:
            return query

        query_lower = query.lower()
        if query_lower in self.words_cap:
            return self.words_cap[query_lower]

        query_vowel = self.devowel(query_lower)
        if query_vowel in self.words_vowel:
            return self.words_vowel[query_vowel]

        return ''
