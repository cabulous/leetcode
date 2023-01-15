class ArrayReader(object):
    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left = 0
        length = reader.length()

        while length > 1:
            length //= 2
            compare = reader.compareSub(
                left,
                left + length - 1,
                left + length,
                left + length + length - 1,
            )

            if compare == 0:
                return left + length + length

            if compare < 0:
                left += length

        return left
