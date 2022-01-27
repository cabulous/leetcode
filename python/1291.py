from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = '123456789'
        length_low, length_high = len(str(low)), len(str(high))
        length_max = 10
        res = []

        for length in range(length_low, length_high + 1):
            for start in range(length_max - length):
                num = int(sample[start:start + length])
                if low <= num <= high:
                    res.append(num)

        return res


class Seqs:

    def __init__(self):
        self.res = []
        self._run()

    def _run(self):
        sample = '123456789'
        length_max = 10
        for length in range(2, length_max):
            for start in range(length_max - length):
                num = int(sample[start:start + length])
                self.res.append(num)

    def get_seqs(self):
        return self.res


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seqs = Seqs().get_seqs()
        return [num for num in seqs if low <= num <= high]
