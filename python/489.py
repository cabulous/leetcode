class Robot:
    def move(self):
        pass

    def turnLeft(self):
        pass

    def turnRight(self):
        pass

    def clean(self):
        pass


# https://leetcode.com/problems/robot-room-cleaner/discuss/150132/Very-clear-Python-DFS-code-beat-99-+/197801
class Solution:

    def __init__(self):
        self.robot = None
        self.visited = set()

    def cleanRoom(self, robot: Robot):
        self.robot = robot
        self.dfs(0, 0, 0, 1)

    def dfs(self, x, y, dx, dy):
        self.robot.clean()
        self.visited.add((x, y))

        for _ in range(4):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in self.visited and self.robot.move():
                self.dfs(nx, ny, dx, dy)
            self.robot.turnLeft()
            dx, dy = -dy, dx

        self.robot.turnLeft()
        self.robot.turnLeft()
        self.robot.move()
        self.robot.turnLeft()
        self.robot.turnLeft()
