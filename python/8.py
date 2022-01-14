INT_MAX = pow(2, 31) - 1
INT_MIN = -pow(2, 31)


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        index = 0
        n = len(s)
        res = 0

        while index < n and s[index] == ' ':
            index += 1

        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1

        while index < n and s[index].isdigit():

            digit = int(s[index])
            is_res_overflow = res > INT_MAX // 10
            is_sum_overflow = res == INT_MAX // 10 and digit > INT_MAX % 10

            if is_res_overflow or is_sum_overflow:
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + digit
            index += 1

        return sign * res


class StateMachine:

    def __init__(self):
        self.state = {
            'q0': 1,
            'q1': 2,
            'q2': 3,
            'qd': 4,
        }
        self.INT_MAX = pow(2, 31) - 1
        self.INT_MIN = -pow(2, 31)
        self._current_state = self.state['q0']
        self._res = 0
        self._sign = 1

    def to_state_q1(self, ch):
        self._sign = -1 if ch == '-' else 1
        self._current_state = self.state['q1']

    def to_state_q2(self, digit):
        self._current_state = self.state['q2']
        self.append_digit(digit)

    def to_state_qd(self):
        self._current_state = self.state['qd']

    def append_digit(self, digit):
        res_overflow = self._res > self.INT_MAX // 10
        sum_overflow = self._res == self.INT_MAX // 10 and digit > self.INT_MAX % 10

        if res_overflow or sum_overflow:
            if self._sign == 1:
                self._res = self.INT_MAX
            else:
                self._res = self.INT_MIN
                self._sign = 1
            self.to_state_qd()
        else:
            self._res = self._res * 10 + digit

    def transition(self, ch):
        if self._current_state == self.state['q0']:
            if ch == ' ':
                return

            if ch in '+-':
                self.to_state_q1(ch)
            elif ch.isdigit():
                self.to_state_q2(int(ch))
            else:
                self.to_state_qd()

        elif self._current_state in (self.state['q1'], self.state['q2']):
            if ch.isdigit():
                self.to_state_q2(int(ch))
            else:
                self.to_state_qd()

    def get_integer(self):
        return self._sign * self._res

    def get_state(self):
        return self._current_state


class Solution:

    def myAtoi(self, s: str) -> int:
        state_machine = StateMachine()

        for ch in s:
            state_machine.transition(ch)
            if state_machine.get_state() == state_machine.state['qd']:
                break

        return state_machine.get_integer()
