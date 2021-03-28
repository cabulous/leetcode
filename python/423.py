from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        out = {
            '0': c['z'],
            '2': c['w'],
            '4': c['u'],
            '6': c['x'],
            '8': c['g'],
        }
        out['3'] = c['h'] - out['8']
        out['5'] = c['f'] - out['4']
        out['7'] = c['s'] - out['6']
        out['9'] = c['i'] - out['5'] - out['6'] - out['8']
        out['1'] = c['n'] - out['7'] - 2 * out['9']
        output = [key * out[key] for key in sorted(out.keys())]
        return ''.join(output)
