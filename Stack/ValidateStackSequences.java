import java.util.*;

// Leetcode Problem 946
public class ValidateStackSequences {

    // O(1) Space O(N) Time
    public boolean validateStackSequencesWithoutStack(int[] pushed, int[] popped) {
        int i = 0, j = 0;
        for (int num : pushed) {
            pushed[i++] = num;
            while (i > 0 && pushed[i - 1] == popped[j]) {
                i--;
                j++;
            }
        }
        return i == 0;
    }

    // O(N) Space and Time
    public boolean validateStackSequencesWithStack(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>();
        int k = 0;
        int n = popped.length;
        for (int nums : pushed) {
            stack.push(nums);
            while (stack.size() > 0 && k < n && popped[k] == stack.peek()) {
                stack.pop();
                k++;
            }
        }
        return stack.size() == 0;
    }
}
