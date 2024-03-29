from collections import Counter
from itertools import combinations, permutations


# https://leetcode.com/problems/longest-subsequence-repeated-k-times/discuss/1471930/Python-Answer-is-not-so-long-explained
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        hot = ''.join(ch * (freq // k) for ch, freq in Counter(s).items())

        combs = set()
        for length in range(len(hot) + 1):
            for cand in combinations(hot, length):
                for perm in permutations(cand):
                    combs.add(''.join(perm))

        combs = sorted(combs, key=lambda x: (len(x), x), reverse=True)
        for c in combs:
            if self.is_sub_seq(c * k, s):
                return c

    def is_sub_seq(self, str1, str2):
        str2 = iter(str2)
        return all(ch in str2 for ch in str1)
