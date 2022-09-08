from enum import IntEnum


class CartType(IntEnum):
    BIG = 1
    MEDIUM = 2
    SMALL = 3


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_capacity = big
        self.big_usage = 0
        self.medium_capacity = medium
        self.medium_usage = 0
        self.small_capacity = small
        self.small_usage = 0

    def addCar(self, carType: int) -> bool:
        if carType == CartType.BIG.value and self.big_usage < self.big_capacity:
            self.big_usage += 1
            return True
        if carType == CartType.MEDIUM.value and self.medium_usage < self.medium_capacity:
            self.medium_usage += 1
            return True
        if carType == CartType.SMALL.value and self.small_usage < self.small_capacity:
            self.small_usage += 1
            return True
        return False
