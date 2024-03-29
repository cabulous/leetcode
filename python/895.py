from collections import Counter, defaultdict


class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.freq_to_vals = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.freq_to_vals[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        val = self.freq_to_vals[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.freq_to_vals[self.max_freq]:
            self.max_freq -= 1
        return val
