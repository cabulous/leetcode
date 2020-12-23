import java.util.PriorityQueue;

// 703. Kth Largest Element in a Stream
public class KthLargest {
    PriorityQueue<Integer> q;
    int k;

    public KthLargest(int k, int[] nums) {
        this.q = new PriorityQueue<>(k);
        this.k = k;

        for (int n : nums) {
            add(n);
        }
    }

    public int add(int val) {
        if (q.size() < k) {
            q.offer(val);
        } else if (val > q.peek()) {
            q.remove();
            q.offer(val);
        }
        return q.peek();
    }
}
