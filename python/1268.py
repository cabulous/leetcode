import bisect
from typing import List


# https://leetcode.com/problems/search-suggestions-system/discuss/436674/C%2B%2BJavaPython-Sort-and-Binary-Search-the-Prefix
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ''
        i = 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            i = self.binary_search(products, prefix)
            res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
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
        self.sub = {}
        self.suggestion = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for product in sorted(products):
            self.insert(product, root)
        return self.search(searchWord, root)

    def insert(self, product, root):
        trie = root
        for char in product:
            if char not in trie.sub:
                trie.sub[char] = Trie()
            trie = trie.sub[char]
            trie.suggestion.append(product)
            trie.suggestion.sort()
            if len(trie.suggestion) > 3:
                trie.suggestion.pop()

    def search(self, search_word, root):
        res = []
        for c in search_word:
            if root:
                root = root.sub.get(c)
            res.append(root.suggestion if root else [])
        return res
