class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength

        for bitmask in range(1 << n):
            if bin(bitmask).count('1') == k:
                curr = [characters[i] for i in range(n) if bitmask & (1 << n - i - 1)]
                self.combinations.append(''.join(curr))

    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return len(self.combinations) > 0
