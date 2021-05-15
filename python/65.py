class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ['+', '-']:
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            elif c in ['e', 'E']:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit


class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7}
        ]

        curr_state = 0

        for c in s:
            if c.isdigit():
                group = 'digit'
            elif c in ['+', '-']:
                group = 'sign'
            elif c in ['e', 'E']:
                group = 'exponent'
            elif c == '.':
                group = 'dot'
            else:
                return False

            if group not in dfa[curr_state]:
                return False

            curr_state = dfa[curr_state][group]

        return curr_state in [1, 4, 7]
