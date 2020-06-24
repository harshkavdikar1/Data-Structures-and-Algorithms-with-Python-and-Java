import java.util.*;

class SolutionLC40 {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {

        List<List<Integer>> result = new ArrayList<List<Integer>>();

        Arrays.sort(candidates);

        helper(candidates, target, new ArrayList<Integer>(), result, 0);

        return result;
    }

    public void helper(int[] candidates, int target, ArrayList<Integer> arr, List<List<Integer>> result, int start) {

        if (target == 0)
            result.add(new ArrayList<Integer>(arr));
        else {
            for (int i = start; i < candidates.length; i++) {
                if (candidates[i] > target)
                    return;
                if (i > start && candidates[i] == candidates[i - 1])
                    continue;
                arr.add(candidates[i]);
                helper(candidates, target - candidates[i], arr, result, i + 1);
                arr.remove(arr.size() - 1);
            }
        }
    }
}

public class CombinationSum2LC40 {
    public static void main(String[] args) {
        SolutionLC40 solution = new SolutionLC40();

        int candidates[] = { 10, 1, 2, 7, 6, 1, 5 };
        int target = 8;

        System.out.println(solution.combinationSum2(candidates, target));

        // Sample output should be
        // [
        // [1, 7],
        // [1, 2, 5],
        // [2, 6],
        // [1, 1, 6]
        // ]
    }
}