# simulation
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num & 1 == 0:
                num >>= 1
            else:
                num -= 1
            steps += 1
        return steps


# Counting Bits - bitwise
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        steps = 0
        power_of_two = 1

        while power_of_two <= num:
            if (power_of_two & num) != 0:
                steps += 2
            else:
                steps += 1
            power_of_two *= 2

        return steps - 1


# Counting Bits - string
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        # Get the binary for num, as a String. Remove the "0b" off the start with splice.
        binary = bin(num)[2:]

        for bit in binary:
            if bit == "1":
                steps += 2
            else:
                steps += 1
        # We need to subtract 1, because the last bit was over-counted.
        return steps - 1
