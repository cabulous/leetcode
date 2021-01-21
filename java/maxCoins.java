class Solution {
    public int maxCoins(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int n = nums.length + 2;
        int[] new_nums = new int[n];

        for (int i = 0; i < nums.length; i++) {
            new_nums[i + 1] = nums[i];
        }

        new_nums[0] = new_nums[n - 1] = 1;

        int[][] dp = new int[n][n];

        for (int left = n - 2; left >= 0; left--) {
            for (int right = left + 2; right < n; right++) {
                for (int i = left + 1; i < right; i++) {
                    dp[left][right] = Math.max(
                            dp[left][right],
                            new_nums[left] * new_nums[i] * new_nums[right] + dp[left][i] + dp[i][right]
                    );
                }
            }
        }

        return dp[0][n - 1];
    }
}

