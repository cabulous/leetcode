import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[swap_idx], self.array[i] = self.array[i], self.array[swap_idx]
        return self.array


class Solution:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        aux = list(self.array)
        for i in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[i] = aux.pop(remove_idx)
        return self.array
