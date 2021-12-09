class Solution {
    public int singleNonDuplicate(int[] nums) {
        int lo = 0;
        int hi = nums.length - 1;

        while (lo < hi) {
            int mi = lo + (hi - lo) / 2;
            if (mi % 2 == 1) {
                mi -= 1;
            }
            if (nums[mi] == nums[mi + 1]) {
                lo = mi + 2;
            } else {
                hi = mi - 1;
            }
        }

        return nums[lo];
    }
}