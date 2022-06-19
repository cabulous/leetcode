import bisect
from typing import List


# https://leetcode.com/problems/search-suggestions-system/discuss/436674/C%2B%2BJavaPython-Sort-and-Binary-Search-the-Prefix
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prefix = ''
        res = []

        products.sort()

        for ch in searchWord:
            prefix += ch
            index = bisect.bisect_left(products, prefix)
            res.append([w for w in products[index:index + 3] if w.startswith(prefix)])

        return res
