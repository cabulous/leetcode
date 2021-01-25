from typing import List

# bit
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        x = 0
        for num in nums:
            x = (x << 1) | num
        if x == 0 or k == 0:
            return True
        while x & 1 == 0:
            x = x >> 1
        while x != 1:
            x = x >> 1
            count = 0
            while x & 1 == 0:
                x = x >> 1
                count += 1
            if count < k:
                return False
        return True


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for num in nums:
            if num == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
        return True
