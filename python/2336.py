class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.smaller = set()

    def popSmallest(self) -> int:
        if self.smaller:
            res = min(self.smaller)
            self.smaller.remove(res)
            return res
        res = self.curr
        self.curr += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.curr:
            self.smaller.add(num)
