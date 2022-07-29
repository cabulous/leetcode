from typing import List


# https://leetcode.com/problems/flatten-2d-vector/discuss/168602/Python-iterator-Solution/934803
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.gen = self._generator(vec)
        self.next_val = next(self.gen, None)

    def _generator(self, vec: List[List[int]]):
        for row in vec:
            for col in row:
                yield col

    def next(self) -> int:
        res = self.next_val
        self.next_val = next(self.gen, None)
        return res

    def hasNext(self) -> bool:
        return self.next_val is not None
