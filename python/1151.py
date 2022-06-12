from typing import List
from collections import deque


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        one_count = 0
        one_max = 0

        left = right = 0
        while right < len(data):
            one_count += data[right]
            right += 1
            if right - left > ones:
                one_count -= data[left]
                left += 1
            one_max = max(one_max, one_count)

        return ones - one_max


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        one_count = 0
        one_max = 0
        queue = deque()

        for num in data:
            one_count += num
            queue.append(num)
            if len(queue) > ones:
                one_count -= queue.popleft()
            one_max = max(one_max, one_count)

        return ones - one_max
