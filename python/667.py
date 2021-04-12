from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n - k))
        for i in range(k + 1):
            if i & 1 == 0:
                ans.append(n - k + i // 2)
            else:
                ans.append(n - i // 2)
        return ans


# https://leetcode.com/problems/beautiful-arrangement-ii/discuss/106955/Short%2Bsimple-with-explanation
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n + 1))
        for i in range(1, k):
            ans[i:] = ans[:i - 1:-1]
        return ans
