from typing import List


# https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/Python%3A-Well-commented-solution-using-Segment-Trees
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = self.right = None


class NumArray:
    def __init__(self, nums: List[int]):
        self.root = self.create_tree(nums, 0, len(nums) - 1)

    def create_tree(self, nums, left, right):
        if left > right:
            return None

        if left == right:
            node = Node(left, right)
            node.total = nums[left]
            return node

        mid = left + (right - left) // 2
        node = Node(left, right)
        node.left = self.create_tree(nums, left, mid)
        node.right = self.create_tree(nums, mid + 1, right)
        node.total = node.left.total + node.right.total

        return node

    def update_val(self, node, index, val):
        if node.start == node.end:
            node.total = val
            return val

        mid = node.start + (node.end - node.start) // 2

        if index <= mid:
            self.update_val(node.left, index, val)
        else:
            self.update_val(node.right, index, val)

        node.total = node.left.total + node.right.total

        return node.total

    def update(self, index: int, val: int) -> None:
        return self.update_val(self.root, index, val)

    def range_sum(self, node, left, right):
        if node.start == left and node.end == right:
            return node.total

        mid = node.start + (node.end - node.start) // 2

        if right <= mid:
            return self.range_sum(node.left, left, right)
        if left >= mid + 1:
            return self.range_sum(node.right, left, right)
        return self.range_sum(node.left, left, mid) + self.range_sum(node.right, mid + 1, right)

    def sumRange(self, left: int, right: int) -> int:
        return self.range_sum(self.root, left, right)
