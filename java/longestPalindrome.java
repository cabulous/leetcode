// https://leetcode.com/problems/longest-palindromic-substring/discuss/2928/Very-simple-clean-java-solution
class Solution {
    private int lo, maxLen;

    public String longestPalindrome(String s) {
        int len = s.length();
        if (len < 2) {
            return s;
        }
        for (int i = 0; i < len - 1; i++) {
            helper(s, i, i);
            helper(s, i, i+1);
        }
        return s.substring(lo, lo + maxLen);
    }

    private void helper(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        if (maxLen < r - l - 1) {
            lo = l + 1;
            maxLen = r - l - 1;
        }
    }
}