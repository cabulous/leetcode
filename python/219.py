from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = set()
        for i, num in enumerate(nums):
            if num in lookup:
                return True
            lookup.add(num)
            if len(lookup) > k:
                lookup.remove(nums[i - k])
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = defaultdict(list)
        for i, num in enumerate(nums):
            if len(lookup[num]) > 0 and i - lookup[num][-1] <= k:
                return True
            lookup[num].append(i)
        return False
