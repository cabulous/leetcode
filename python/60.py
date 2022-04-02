class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]
        nums = ['1']
        for i in range(1, n):
            factorials.append(factorials[-1] * i)
            nums.append(str(i + 1))

        k -= 1
        res = []

        for i in reversed(range(n)):
            index = k // factorials[i]
            k -= index * factorials[i]
            res.append(nums[index])
            del nums[index]

        return ''.join(res)
