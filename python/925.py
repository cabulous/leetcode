class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_idx = 0

        for typed_idx in range(len(typed)):
            if name_idx < len(name) and name[name_idx] == typed[typed_idx]:
                name_idx += 1
            elif typed_idx == 0 or typed[typed_idx] != typed[typed_idx - 1]:
                return False

        return name_idx == len(name)
