class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        facing = 0

        for i in instructions:
            if i == 'L':
                facing = (facing + 3) % 4
            elif i == 'R':
                facing = (facing + 1) % 4
            else:
                dx, dy = directions[facing]
                x += dx
                y += dy

        return (x == 0 and y == 0) or facing != 0
