from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped_index = 0

        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[popped_index]:
                popped_index += 1
                stack.pop()

        return len(stack) == 0
