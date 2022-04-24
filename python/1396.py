from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {}
        self.journey = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in_data.pop(id)
        time = t - start_time
        self.journey[start_station, stationName][0] += 1
        self.journey[start_station, stationName][1] += time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_trip, total_time = self.journey[startStation, endStation]
        return total_time / total_trip
