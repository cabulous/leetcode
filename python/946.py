from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped_idx = 0

        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[popped_idx]:
                popped_idx += 1
                stack.pop()

        return not stack
