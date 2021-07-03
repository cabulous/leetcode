import bisect
from typing import List


# https://leetcode.com/problems/search-suggestions-system/discuss/436674/C%2B%2BJavaPython-Sort-and-Binary-Search-the-Prefix
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            idx = bisect.bisect_left(products, prefix)
            res.append([w for w in products[idx:idx + 3] if w.startswith(prefix)])
        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            idx = self.binary_search(products, prefix)
            res.append([w for w in products[idx:idx + 3] if w.startswith(prefix)])
        return res

    def binary_search(self, array, target):
        lo, hi = 0, len(array)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if array[mi] < target:
                lo = mi + 1
            else:
                hi = mi
        return lo


# https://leetcode.com/problems/search-suggestions-system/discuss/436151/JavaPython-3-Simple-Trie-and-Binary-Search-codes-w-comment-and-brief-analysis.
class Trie:
    def __init__(self):
        self.next = {}
        self.suggestion = []


class Solution:
    def __init__(self):
        self.root = Trie()

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        for product in sorted(products):
            self.insert(product)
        return self.search(searchWord)

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = Trie()
            node = node.next[c]
            node.suggestion.append(word)
            node.suggestion.sort()
            if len(node.suggestion) > 3:
                node.suggestion.pop()

    def search(self, word):
        node = self.root
        ans = []
        for c in word:
            if node:
                node = node.next.get(c)
            ans.append(node.suggestion if node else [])
        return ans
