import java.util.*;

// Leetcode Problem 496
public class NextGreaterElement {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        for (int num:nums2) {
            while (stack.size()>0 && stack.peek() < num) {
                int x = stack.pop();
                map.put(x, num);
            }
            stack.push(num);
        }
        for (int i=0; i<nums1.length; i++) {
            nums1[i] = map.getOrDefault(nums1[i], -1);
        }
        return nums1;
    }
}

