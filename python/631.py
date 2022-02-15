import string
from collections import Counter
from typing import List


# https://leetcode.com/problems/design-excel-sum-formula/discuss/104862/Python-Solution/422272
class Excel:

    def __init__(self, height: int, width: str):
        self.cells = [{letter: {'val': 0, 'sum': None} for letter in string.ascii_uppercase} for _ in range(height + 1)]

    def set(self, row: int, column: str, val: int) -> None:
        self.cells[row][column] = {'val': val, 'sum': None}

    def get(self, row: int, column: str) -> int:
        cell = self.cells[row][column]
        address = cell.get('sum')
        if address is None:
            return cell.get('val', 0)
        return sum(self.get(*addr) * count for addr, count in address.items())

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.cells[row][column]['sum'] = self._parse(numbers)
        return self.get(row, column)

    def _parse(self, strs: List[str]):
        counter = Counter()
        for s in strs:
            start, end = s.split(':')[0], s.split(':')[1] if ':' in s else s
            for r in range(int(start[1:]), int(end[1:]) + 1):
                for c in range(ord(start[0]), ord(end[0]) + 1):
                    counter[(r, chr(c))] += 1
        return counter
