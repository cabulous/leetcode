from typing import List


# https://leetcode.com/problems/find-the-duplicate-number/discuss/704693/Python-2-solutions%3A-Linked-List-Cycle-O(n)-and-BS-O(n-log-n)-explained
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow


# https://leetcode.com/problems/find-the-duplicate-number/discuss/704693/Python-2-solutions:-Linked-List-Cycle-O(n)-and-BS-O(n-log-n)-explained/593157
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bits = 0
        for num in nums:
            if bits & (1 << num) != 0:
                return num
            bits |= (1 << num)
