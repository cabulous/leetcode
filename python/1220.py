class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a_count = [1] * n
        e_count = [1] * n
        i_count = [1] * n
        o_count = [1] * n
        u_count = [1] * n

        for i in range(1, n):
            a_count[i] = (e_count[i - 1] + i_count[i - 1] + u_count[i - 1]) % mod
            e_count[i] = (a_count[i - 1] + i_count[i - 1]) % mod
            i_count[i] = (e_count[i - 1] + o_count[i - 1]) % mod
            o_count[i] = (i_count[i - 1]) % mod
            u_count[i] = (i_count[i - 1] + o_count[i - 1]) % mod

        return (a_count[-1] + e_count[-1] + i_count[-1] + o_count[-1] + u_count[-1]) % mod
