import java.util.*;

class Solution {
    public int pseudoPalindromicPaths(TreeNode root) {
        int count = 0;
        int path = 0;
        Deque<Pair<TreeNode, Integer>> stack = new ArrayDeque<>();
        stack.push(new Pair(root, 0));
        while (!stack.isEmpty()) {
            Pair<TreeNode, Integer> p = stack.pop();
            TreeNode node = p.getKey();
            path = p.getValue();
            if (node != null) {
                path ^= (1 << node.val);
                if (node.left == null && node.right == null) {
                    if ((path & (path - 1)) == 0) {
                        count++;
                    }
                } else {
                    stack.push(new Pair(node.left, path));
                    stack.push(new Pair(node.right, path));
                }
            }
        }
        return count;
    }
}