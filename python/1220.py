MOD = 10 ** 9 + 7


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a_count = [1] * n
        e_count = [1] * n
        i_count = [1] * n
        o_count = [1] * n
        u_count = [1] * n

        for i in range(1, n):
            a_count[i] = (e_count[i - 1] + i_count[i - 1] + u_count[i - 1]) % MOD
            e_count[i] = (a_count[i - 1] + i_count[i - 1]) % MOD
            i_count[i] = (e_count[i - 1] + o_count[i - 1]) % MOD
            o_count[i] = (i_count[i - 1]) % MOD
            u_count[i] = (i_count[i - 1] + o_count[i - 1]) % MOD

        return (a_count[-1] + e_count[-1] + i_count[-1] + o_count[-1] + u_count[-1]) % MOD
