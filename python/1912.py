import heapq
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/design-movie-rental-system/discuss/1298481/Python3-priority-queues
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(list)
        self.available = {}
        self.price = {}
        self.rented = []

        for shop, movie, price in entries:
            heapq.heappush(self.movies[movie], (price, shop))
            self.available[shop, movie] = True
            self.price[shop, movie] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.movies:
            return []

        res = []
        temp = []

        while len(res) < 5 and self.movies[movie]:
            price, shop = heapq.heappop(self.movies[movie])
            temp.append((price, shop))
            if self.available[shop, movie]:
                res.append(shop)

        for price, shop in temp:
            heapq.heappush(self.movies[movie], (price, shop))

        return res

    def rent(self, shop: int, movie: int) -> None:
        self.available[shop, movie] = False
        price = self.price[shop, movie]
        heapq.heappush(self.rented, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.available[shop, movie] = True

    def report(self) -> List[List[int]]:
        res = []

        while len(res) < 5 and self.rented:
            price, shop, movie = heapq.heappop(self.rented)
            if not self.available[shop, movie] and (price, shop, movie) not in res:
                res.append((price, shop, movie))

        for price, shop, movie in res:
            heapq.heappush(self.rented, (price, shop, movie))

        return [[shop, movie] for _, shop, movie in res]
