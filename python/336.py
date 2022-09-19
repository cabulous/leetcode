from collections import defaultdict
from typing import List


# hashing
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_lookup = {w: i for i, w in enumerate(words)}
        res = []

        for word_idx, word in enumerate(words):
            reversed_word = word[::-1]
            if reversed_word in word_lookup and word_lookup[reversed_word] != word_idx:
                res.append([word_idx, word_lookup[reversed_word]])

            for prefix in self.valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    res.append([word_idx, word_lookup[reversed_prefix]])

            for suffix in self.valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    res.append([word_lookup[reversed_suffix], word_idx])

        return res

    def valid_prefixes(self, word):
        for i in range(len(word)):
            if word[i:] == word[i:][::-1]:
                yield word[:i]

    def valid_suffixes(self, word):
        for i in range(len(word)):
            if word[:i + 1] == word[:i + 1][::-1]:
                yield word[i + 1:]


# trie
class TrieNode:
    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.ending_word = -1
        self.palindrome_suffixes = []


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = TrieNode()

        for i, word in enumerate(words):
            word = word[::-1]
            current_level = trie
            for j, c in enumerate(word):
                if word[j:] == word[j:][::-1]:
                    current_level.palindrome_suffixes.append(i)
                current_level = current_level.next[c]
            current_level.ending_word = i

        res = []

        for i, word in enumerate(words):
            current_level = trie
            for j, c in enumerate(word):
                if current_level.ending_word != -1:
                    if word[j:] == word[j:][::-1]:
                        res.append([i, current_level.ending_word])
                if c not in current_level.next:
                    break
                current_level = current_level.next[c]
            else:
                if current_level.ending_word != -1 and current_level.ending_word != i:
                    res.append([i, current_level.ending_word])
                for j in current_level.palindrome_suffixes:
                    res.append([i, j])

        return res
