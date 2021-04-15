from typing import List
from collections import deque


# Sliding Window with Two Pointers
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cnt_one = max_one = 0
        left = right = 0
        while right < len(data):
            cnt_one += data[right]
            right += 1
            if right - left > ones:
                cnt_one -= data[left]
                left += 1
            max_one = max(max_one, cnt_one)
        return ones - max_one


# Sliding Window with Deque
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cnt_one = max_one = 0
        q = deque()
        for i in range(len(data)):
            q.append(data[i])
            cnt_one += data[i]
            if len(q) > ones:
                cnt_one -= q.popleft()
            max_one = max(max_one, cnt_one)
        return ones - max_one
