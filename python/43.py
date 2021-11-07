from itertools import zip_longest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        first_number = num1[::-1]
        second_number = num2[::-1]
        ans = [0] * (len(num1) + len(num2))

        for place1, digit1 in enumerate(first_number):
            for place2, digit2 in enumerate(second_number):
                num_zeros = place1 + place2
                carry = ans[num_zeros]
                multiplication = int(digit1) * int(digit2) + carry
                ans[num_zeros] = multiplication % 10
                ans[num_zeros + 1] += multiplication // 10

        if ans[-1] == 0:
            ans.pop()

        return ''.join(str(digit) for digit in reversed(ans))


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        first_number = num1[::-1]
        second_number = num2[::-1]

        results = []
        for index, digit in enumerate(second_number):
            results.append(self.multiply_one_digit(digit, index, first_number))

        answer = self.sum_results(results)

        return ''.join(str(digit) for digit in reversed(answer))

    def multiply_one_digit(self, digit2, num_zeros, first_number):
        cur_res = [0] * num_zeros
        carry = 0

        for digit1 in first_number:
            multiplication = int(digit1) * int(digit2) + carry
            carry = multiplication // 10
            cur_res.append(multiplication % 10)

        if carry != 0:
            cur_res.append(carry)

        return cur_res

    def sum_results(self, results):
        answer = results.pop()

        for result in results:
            new_answer = []
            carry = 0

            for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
                cur_sum = digit1 + digit2 + carry
                carry = cur_sum // 10
                new_answer.append(cur_sum % 10)

            if carry != 0:
                new_answer.append(carry)

            answer = new_answer

        return answer
