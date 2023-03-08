import bisect
from collections import defaultdict


# https://leetcode.com/problems/shortest-way-to-form-string/solutions/304662/python-o-m-n-logm-using-inverted-index-binary-search-similar-to-lc-792/
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        lookup = defaultdict(list)
        for i, ch in enumerate(source):
            lookup[ch].append(i)

        read_idx = -1
        res = 1

        for ch in target:
            if ch not in lookup:
                return -1

            idx_list = lookup[ch]
            found_idx = bisect.bisect_left(idx_list, read_idx)

            if found_idx == len(idx_list):
                res += 1
                read_idx = idx_list[0] + 1
            else:
                read_idx = idx_list[found_idx] + 1

        return res
