from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.checkin_data = {}
        self.journey = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkin_data.pop(id)
        duration = t - start_time
        self.journey[start_station, stationName][0] += 1
        self.journey[start_station, stationName][1] += duration

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip, duration = self.journey[startStation, endStation]
        return duration / trip
