import java.util.*;

/**
 * Leetcode problem 503
 */
public class NextGreaterElement2 {
    public int[] nextGreaterElements(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[nums.length];
        int n = nums.length;
        Arrays.fill(result, -1);
        for (int i = 0; i < n * 2; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i % n])
                result[stack.pop()] = nums[i % n];
            stack.push(i % n);
        }
        return result;
    }
}
