from typing import List


class Solution:

    def __init__(self):
        self.reversible_pairs = [['0', '0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]
        self.final_length = 0

    def findStrobogrammatic(self, n: int) -> List[str]:
        self.final_length = n
        return self.helper(n)

    def helper(self, curr_length):
        if curr_length == 0:
            return ['']

        if curr_length == 1:
            return ['0', '1', '8']

        prev_strobo_nums = self.helper(curr_length - 2)
        curr_strobo_nums = []

        for num in prev_strobo_nums:
            for first, last in self.reversible_pairs:
                if first != '0' or curr_length != self.final_length:
                    curr_strobo_nums.append(first + num + last)

        return curr_strobo_nums


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversible_pairs = [['0', '0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]
        curr_length = n % 2
        curr = [''] if curr_length == 0 else ['0', '1', '8']

        while curr_length < n:
            nxt = []
            curr_length += 2
            for num in curr:
                for first, last in reversible_pairs:
                    if first != '0' or curr_length != n:
                        nxt.append(first + num + last)
            curr = nxt

        return curr
