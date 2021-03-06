from typing import List


# remove suffix words
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)


# trie
# https://leetcode.com/problems/short-encoding-of-words/discuss/125784/Trie-Solution
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = dict()
        leaves = []
        for word in set(words):
            cur = root
            for i in word[::-1]:
                cur[i] = cur = cur.get(i, dict())
            leaves.append((cur, len(word) + 1))
        return sum(depth for node, depth in leaves if len(node) == 0)
