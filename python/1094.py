from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = []

        for passenger_count, start, end in trips:
            stops.append([start, passenger_count])
            stops.append([end, -passenger_count])

        stops.sort()

        used_capacity = 0

        for _, passenger_change in stops:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
