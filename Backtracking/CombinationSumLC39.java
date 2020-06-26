import java.util.*;

class SolutionLC39 {
    public List<List<Integer>> combinationSum(final int[] candidates, final int target) {
        Arrays.sort(candidates);

        final List<List<Integer>> result = new ArrayList<List<Integer>>();

        helper(candidates, target, new ArrayList<Integer>(), result, 0);

        return result;
    }

    public void helper(final int[] candidates, final int target, final ArrayList<Integer> arr,
            final List<List<Integer>> result, final int start) {

        if (target == 0) {
            result.add(new ArrayList<Integer>(arr));
        } else {
            for (int index = start; index < candidates.length; index++) {
                if (candidates[index] > target)
                    return;
                arr.add(candidates[index]);
                helper(candidates, target - candidates[index], arr, result, index);
                arr.remove(arr.size() - 1);
            }
        }
    }
}

public class CombinationSumLC39 {

    public static void main(final String[] args) {
        SolutionLC39 solution = new SolutionLC39();

        int candidates[] = { 2, 3, 5 };
        int target = 8;

        System.out.println(solution.combinationSum(candidates, target));
    }

}