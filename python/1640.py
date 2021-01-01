# https://leetcode.com/problems/check-array-formation-through-concatenation/discuss/918408/Python-5-lines-hashmap
class Solution:
    def canFormArray(self, arr: [int], pieces: [[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        res = []
        for num in arr:
            res += mp.get(num, [])
        return res == arr


class Solution:
    def canFormArray(self, arr: [int], pieces: [[int]]) -> bool:
        n = len(arr)
        mapping = {p[0]: p for p in pieces}

        i = 0
        while i < n:
            if arr[i] not in mapping:
                return False
            target_piece = mapping[arr[i]]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1

        return True
