import java.util.Arrays;

class Solution {
    public boolean increasingTriplet(int[] nums) {
        return increasingKNums(nums, 3);
    }

    private boolean increasingKNums(int[] nums, int k) {
        if (k == 0) {
            return true;
        }
        int[] inc = new int[k - 1];
        Arrays.fill(inc, Integer.MAX_VALUE);
        for (int n : nums) {
            int index = k;
            for (int i = 0; i < inc.length; i++) {
                if (n <= inc[i]) {
                    index = i;
                    break;
                }
            }
            if (index >= k - 1) {
                return true;
            }
            inc[index] = n;
        }
        return false;
    }
}