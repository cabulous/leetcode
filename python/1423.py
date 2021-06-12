from typing import List


# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597763/Python3-Easy-Sliding-Window-O(n):-Find-minimum-subarray/517081
# Sliding Window
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr = sum(cardPoints[:k])
        res = curr
        for i in range(1, k + 1):
            curr += (cardPoints[-i] - cardPoints[k - i])
            res = max(res, curr)
        return res


# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597763/Python3-Easy-Sliding-Window-O(n)%3A-Find-minimum-subarray
# Sliding Window
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        min_sub_array = curr = sum(cardPoints[:size])
        for i in range(k):
            curr += cardPoints[size + i] - cardPoints[i]
            min_sub_array = min(min_sub_array, curr)
        return sum(cardPoints) - min_sub_array
