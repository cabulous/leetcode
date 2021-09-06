from operator import sub
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key, duration = keysPressed[0], releaseTimes[0]

        for i in range(1, len(keysPressed)):
            time = releaseTimes[i] - releaseTimes[i - 1]
            if time > duration or (time == duration and keysPressed[i] > key):
                key = keysPressed[i]
                duration = time

        return key


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        return max(zip(map(sub, releaseTimes, [0, *releaseTimes]), keysPressed))[1]
