from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            if arr[node] < 0:
                continue
            arr[node] *= -1
            for i in [node + arr[node], node - arr[node]]:
                if 0 <= i < len(arr):
                    queue.append(i)

        return False


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            arr[start] *= -1
            return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False
