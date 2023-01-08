from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = 0
        total_damage = 0

        for d in damage:
            max_damage = max(max_damage, d)
            total_damage += d

        return total_damage - min(armor, max_damage) + 1
