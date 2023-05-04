from collections import deque

RADIANT = 'Radiant'
DIRE = 'Dire'


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))

        return RADIANT if radiant else DIRE
