# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392933/JavaC%2B%2BPython-Two-Pointers-and-Stack-Solution
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]

        for ch in s:
            if stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])

        return ''.join(ch * count for ch, count in stack)
