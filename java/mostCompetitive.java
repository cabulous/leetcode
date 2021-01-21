import java.util.Stack;

// https://leetcode.com/problems/find-the-most-competitive-subsequence/discuss/952786/JavaC%2B%2BPython-One-Pass-Stack-Solution
class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[k];
        for (int i = 0; i < nums.length; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i] && stack.size() + nums.length - i > k) {
                stack.pop();
            }
            if (stack.size() < k) {
                stack.add(i);
            }
        }
        for (int i = k - 1; i >= 0; i--) {
            result[i] = nums[stack.pop()];
        }
        return result;
    }
}