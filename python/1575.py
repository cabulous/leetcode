from functools import lru_cache


class Solution:

    def __init__(self):
        self.MOD = 10 ** 9 + 7
        self.dest = 0
        self.locations = []

    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        self.dest = finish
        self.locations = locations
        return self.helper(start, fuel)

    @lru_cache(None)
    def helper(self, city, fuel):
        if fuel < 0:
            return 0

        res = 1 if city == self.dest else 0

        if fuel == 0:
            return res

        for next_city in range(len(self.locations)):
            if city != next_city:
                fuel_needed = abs(self.locations[city] - self.locations[next_city])
                if fuel >= fuel_needed:
                    res += self.helper(next_city, fuel - fuel_needed)
                    res %= self.MOD

        return res


class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [[0] * (fuel + 1) for _ in range(len(locations))]
        for f in range(fuel + 1):
            dp[finish][f] = 1

        for f in range(fuel + 1):
            for city in range(len(locations)):
                for next_city in range(len(locations)):
                    if city != next_city:
                        fuel_needed = abs(locations[city] - locations[next_city])
                        if f >= fuel_needed:
                            dp[city][f] += dp[next_city][f - fuel_needed]
                            dp[city][f] %= MOD

        return dp[start][fuel]
