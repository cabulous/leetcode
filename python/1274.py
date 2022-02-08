class Sea(object):
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        pass


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/441406/Python-Quartered-Search-and-O(1)-hack-for-fun
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        res = 0

        if bottomLeft.x <= topRight.x and bottomLeft.y <= topRight.y and sea.hasShips(topRight, bottomLeft):

            if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
                return 1

            mid_x = (bottomLeft.x + topRight.x) // 2
            mid_y = (bottomLeft.y + topRight.y) // 2

            res += self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1))
            res += self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1))
            res += self.countShips(sea, Point(mid_x, mid_y), bottomLeft)
            res += self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))

        return res
