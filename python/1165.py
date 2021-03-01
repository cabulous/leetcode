class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = dict(zip(list(keyboard), range(len(keyboard))))
        res = 0
        cur_index = 0
        for w in word:
            res += abs(d[w] - cur_index)
            cur_index = d[w]
        return res


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        cur_index = 0
        time = 0
        for w in word:
            next_index = keyboard.index(w)
            time += abs(next_index - cur_index)
            cur_index = next_index
        return time
