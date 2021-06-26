from typing import List


# merge sort
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
class Solution:
    def __init__(self):
        self.smaller = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.smaller = [0] * len(nums)
        self.sort(list(enumerate(nums)))
        return self.smaller

    def sort(self, enum):
        half = len(enum) // 2
        if half:
            left, right = self.sort(enum[:half]), self.sort(enum[half:])
            for i in reversed(range(len(enum))):
                if not right or (left and left[-1][1] > right[-1][1]):
                    self.smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum


# index tree
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        offset = 10 ** 4
        size = 2 * 10 ** 4 + 2
        tree = [0] * size
        res = []

        for num in reversed(nums):
            smaller_counter = self.query(num + offset, tree)
            res.append(smaller_counter)
            self.update(num + offset, 1, tree, size)

        return list(reversed(res))

    def update(self, index, value, tree, size):
        index += 1
        while index < size:
            tree[index] += value
            index += index & -index

    def query(self, index, tree):
        res = 0
        while index >= 1:
            res += tree[index]
            index -= index & -index
        return res


# segment tree
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        offset = 10 ** 4
        size = 2 * 10 ** 4 + 1
        tree = [0] * (2 * size)
        res = []

        for num in reversed(nums):
            smaller_count = self.query(0, num + offset, tree, size)
            res.append(smaller_count)
            self.update(num + offset, 1, tree, size)

        return list(reversed(res))

    def update(self, index, value, tree, size):
        index += size
        tree[index] += value
        while index > 1:
            index //= 2
            tree[index] = tree[index * 2] + tree[index * 2 + 1]

    def query(self, left, right, tree, size):
        res = 0
        left += size
        right += size
        while left < right:
            if left % 2 == 1:
                res += tree[left]
                left += 1
            left //= 2
            if right % 2 == 1:
                right -= 1
                res += tree[right]
            right //= 2
        return res
