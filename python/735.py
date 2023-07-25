class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for size in asteroids:
            if not stack or size > 0:
                stack.append(size)
            else:
                while stack and 0 < stack[-1] < abs(size):
                    stack.pop()
                if stack and stack[-1] == abs(size):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(size)

        return stack
