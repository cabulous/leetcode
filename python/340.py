from collections import defaultdict, OrderedDict


# Sliding Window + Hashmap
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n * k == 0:
            return 0

        left, right = 0, 0
        hashmap = defaultdict()
        max_len = 1

        while right < n:
            hashmap[s[right]] = right
            right += 1
            if len(hashmap) == k + 1:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len, right - left)

        return max_len


# Sliding Window + Ordered Dictionary
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n * k == 0:
            return 0

        left, right = 0, 0
        hashmap = OrderedDict()
        max_len = 1

        while right < n:
            c = s[right]
            if c in hashmap:
                del hashmap[c]
            hashmap[c] = right
            right += 1
            if len(hashmap) == k + 1:
                _, del_idx = hashmap.popitem(last=False)
                left = del_idx + 1
            max_len = max(max_len, right - left)

        return max_len
