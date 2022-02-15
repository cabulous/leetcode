from collections import Counter


# https://leetcode.com/problems/permutation-in-string/discuss/175592/Python-8-lines-Sliding-Window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1, count2 = Counter(s1), Counter(s2[:len(s1)])
        win_size = len(s1)

        for right in range(len(s1), len(s2)):
            if count1 == count2:
                return True

            count2[s2[right]] += 1

            left = right - win_size
            count2[s2[left]] -= 1

            if count2[s2[left]] == 0:
                del count2[s2[left]]

        return count1 == count2
