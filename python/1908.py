class Solution:

    def __init__(self):
        self.memo = {}

    def nimGame(self, piles: list[int]) -> bool:
        return self._is_next_player_winner(piles, sum(piles))

    def _is_next_player_winner(self, piles_state, remaining):
        key = '-'.join(map(str, piles_state))
        if key in self.memo:
            return self.memo[key]

        if remaining == 0:
            return False

        for i in range(len(piles_state)):
            for taken in range(1, piles_state[i] + 1):
                piles_state[i] -= taken
                next_piles_state = sorted(piles_state)
                next_remaining = remaining - taken
                if not self._is_next_player_winner(next_piles_state, next_remaining):
                    self.memo[key] = True
                    return True
                piles_state[i] += taken

        self.memo[key] = False
        return False
