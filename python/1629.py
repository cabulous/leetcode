from operator import sub
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key, duration = keysPressed[0], releaseTimes[0]

        for i in range(1, len(keysPressed)):
            next_duration = releaseTimes[i] - releaseTimes[i - 1]
            if next_duration > duration or (next_duration == duration and keysPressed[i] > key):
                key = keysPressed[i]
                duration = next_duration

        return key


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        return max(zip(map(sub, releaseTimes, [0, *releaseTimes]), keysPressed))[1]
