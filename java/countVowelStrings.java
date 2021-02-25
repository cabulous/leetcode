class Solution {
    public int countVowelStrings(int n) {
        int[][] memo = new int[n + 1][6];
        return helper(n, 5, memo);
    }

    int helper(int n, int vowels, int[][] memo) {
        if (n == 1 || vowels == 1) {
            return vowels;
        }
        if (memo[n][vowels] != 0) {
            return memo[n][vowels];
        }
        memo[n][vowels] = helper(n - 1, vowels, memo) + helper(n, vowels - 1, memo);
        return memo[n][vowels];
    }
}