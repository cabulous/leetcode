class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        left = 1
        right = min(time) * totalTrips

        while left < right:
            mid = left + (right - left) // 2
            if sum(mid // t for t in time) < totalTrips:
                left = mid + 1
            else:
                right = mid

        return left
