from itertools import product
from typing import List


# https://leetcode.com/problems/brace-expansion/discuss/314308/Python-3-line-Using-Product
class Solution:
    def expand(self, s: str) -> List[str]:
        lst = s.replace('{', ' ').replace('}', ' ').strip().split()
        lst = [sorted(a.split(',')) for a in lst]
        return [''.join(item) for item in product(*lst)]
