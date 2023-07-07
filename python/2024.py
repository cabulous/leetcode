from collections import Counter


# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/solutions/1499049/java-c-python-sliding-window-strict-o-n/
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = Counter()
        max_count = 0
        left = 0

        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            max_count = max(max_count, count[answerKey[right]])
            if right - left + 1 > max_count + k:
                count[answerKey[left]] -= 1
                left += 1

        return len(answerKey) - left
