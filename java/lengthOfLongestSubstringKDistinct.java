import java.util.*;

class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int n = s.length();
        if (n * k == 0) {
            return 0;
        }

        int left = 0;
        int right = 0;
        Map<Character, Integer> hashmap = new HashMap<>();
        int maxLen = 1;

        while (right < n) {
            hashmap.put(s.charAt(right), right++);
            if (hashmap.size() == k + 1) {
                int delIdx = Collections.min(hashmap.values());
                hashmap.remove(s.charAt(delIdx));
                left = delIdx + 1;
            }
            maxLen = Math.max(maxLen, right - left);
        }

        return maxLen;
    }
}