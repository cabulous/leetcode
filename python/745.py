from typing import List
from collections import defaultdict

# https://leetcode.com/problems/prefix-and-suffix-search/solution/551448
Trie = lambda: defaultdict(Trie)


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for weight, word in enumerate(words):
            for i in range(len(word) + 1):
                node = self.trie
                node['weight'] = weight
                word_to_insert = word[i:] + '#' + word
                for c in word_to_insert:
                    node = node[c]
                    node['weight'] = weight

    def f(self, prefix: str, suffix: str) -> int:
        node = self.trie
        for c in suffix + '#' + prefix:
            if c not in node:
                return -1
            node = node[c]
        return node['weight']


# https://leetcode.com/problems/prefix-and-suffix-search/discuss/483341/Short-Python
class WordFilter:

    def __init__(self, words: List[str]):
        W = ' '.join(w + '=' + w for w in words[::-1])
        self.f = lambda p, s: W.count('=', W.find(s + '=' + p)) - 1
