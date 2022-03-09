from collections import Counter


# https://leetcode.com/problems/rearrange-string-k-distance-apart/discuss/278269/Python-O(N)-solution
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k:
            return s

        n = len(s)
        count = Counter(s)
        max_val = max(count.values())
        max_val_count = sum(1 for val in count.values() if val == max_val)

        if (max_val - 1) * k + max_val_count > n:
            return ''

        res = list(s)
        i = (n - 1) % k

        for c in sorted(count, key=lambda x: -count[x]):
            for j in range(count[c]):
                res[i] = c
                i += k
                if i >= n:
                    i = (i - 1) % k

        return ''.join(res)
