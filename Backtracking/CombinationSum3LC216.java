import java.util.*;

class SolutionLC216 {
    public List<List<Integer>> combinationSum3(int k, int n) {
        int[] candidates = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

        List<List<Integer>> result = new ArrayList<List<Integer>>();

        helper(candidates, k, n, new ArrayList<Integer>(), result, 0);

        return result;
    }

    public void helper(int[] candidates, int k, int target, ArrayList<Integer> arr, List<List<Integer>> result,
            int start) {
        if (k == 0) {
            if (target == 0)
                result.add(new ArrayList<Integer>(arr));
            return;
        } else {
            for (int i = start; i < candidates.length; i++) {
                if (candidates[i] > target)
                    return;
                arr.add(candidates[i]);
                helper(candidates, k - 1, target - candidates[i], arr, result, i + 1);
                arr.remove(arr.size() - 1);
            }
        }
    }
}

public class CombinationSum3LC216 {
    public static void main(String[] args) {
        SolutionLC216 solution = new SolutionLC216();

        int k = 3;
        int n = 9;

        System.out.println(solution.combinationSum3(k, n));
    }
}