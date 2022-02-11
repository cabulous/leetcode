from collections import defaultdict
from typing import List


# https://leetcode.com/problems/design-search-autocomplete-system/discuss/105386/Python-Clean-Solution-Using-Trie
class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
        self.data = None
        self.rank = 0


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ''
        for i, sentence in enumerate(sentences):
            self.add_record(sentence, times[i])

    def add_record(self, sentence, hot):
        node = self.root
        for c in sentence:
            node = node.children[c]
        node.is_end = True
        node.data = sentence
        node.rank -= hot

    def collect_candidates(self, node):
        if node is None:
            return []

        res = []

        if node.is_end:
            res.append((node.rank, node.data))

        for kid in node.children:
            res.extend(self.collect_candidates(node.children[kid]))

        return res

    def search(self, sentence):
        node = self.root
        for c in sentence:
            if c not in node.children:
                return []
            node = node.children[c]
        return self.collect_candidates(node)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.add_record(self.keyword, 1)
            self.keyword = ''
            return []

        self.keyword += c
        res = self.search(self.keyword)

        return [sentence for _, sentence in sorted(res)[:3]]
