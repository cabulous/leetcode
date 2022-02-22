class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        peak = 0

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
                peak = left
            else:
                right = mid - 1

        left, right = 0, peak
        while left <= right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            elif target < mountain_arr.get(mid):
                right = mid - 1
            else:
                return mid

        left, right = peak, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            elif target > mountain_arr.get(mid):
                right = mid - 1
            else:
                return mid

        return -1
