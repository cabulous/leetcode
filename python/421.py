from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        length = len(bin(max(nums))) - 2
        max_xor = 0

        for i in reversed(range(length)):
            max_xor <<= 1
            cur_xor = max_xor | 1
            prefixes = {num >> i for num in nums}
            max_xor |= any(cur_xor ^ p in prefixes for p in prefixes)

        return max_xor


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        length = len(bin(max(nums))) - 2
        nums = [[(num >> i) & 1 for i in range(length)][::-1] for num in nums]
        max_xor = 0
        trie = {}

        for num in nums:
            node = trie
            xor_node = trie
            cur_xor = 0

            for bit in num:
                if not bit in node:
                    node[bit] = {}
                node = node[bit]
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    cur_xor = (cur_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    cur_xor <<= 1
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, cur_xor)

        return max_xor
