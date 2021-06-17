from collections import defaultdict
from typing import List


# hashing
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes

        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i + 1] == word[:i + 1][::-1]:
                    valid_suffixes.append(word[i + 1:])
            return valid_suffixes

        word_lookup = {word: i for i, word in enumerate(words)}
        res = []

        for word_index, word in enumerate(words):
            reversed_word = word[::-1]
            if reversed_word in word_lookup and word_index != word_lookup[reversed_word]:
                res.append([word_index, word_lookup[reversed_word]])

            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    res.append([word_index, word_lookup[reversed_prefix]])

            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    res.append([word_lookup[reversed_suffix], word_index])

        return res


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
