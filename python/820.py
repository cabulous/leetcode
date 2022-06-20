from typing import List


# remove suffix words
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)

        for word in set(words):
            for i in range(1, len(word)):
                good.discard(word[i:])

        return sum(len(w) + 1 for w in good)


# trie
# https://leetcode.com/problems/short-encoding-of-words/discuss/125784/Trie-Solution
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = dict()
        leaves = []

        for word in set(words):
            curr = trie
            for ch in word[::-1]:
                curr[ch] = curr = curr.get(ch, dict())
            leaves.append((curr, len(word) + 1))

        return sum(depth for node, depth in leaves if len(node) == 0)
