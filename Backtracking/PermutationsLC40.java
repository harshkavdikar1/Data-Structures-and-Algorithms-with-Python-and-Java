import java.util.*;

class Permutation {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        helper(nums, new ArrayList<Integer>(), result);
        
        return result;
    }

    public void helper(int[] nums, ArrayList<Integer> arr, List<List<Integer>> result){
        if(arr.size() == nums.length) result.add(new ArrayList<Integer>(arr));
        else {
            for (int num: nums){
                if (arr.contains(num)) continue;
                arr.add(num);
                helper(nums, arr, result);
                arr.remove(arr.size()-1);
            }
        }
    }
}



public class PermutationsLC40{

    public static void main(String[] args) {
        
        int[] nums = {1,2,3};
        Permutation permutation = new Permutation();
        System.out.println(permutation.permute(nums));
 
    }
}