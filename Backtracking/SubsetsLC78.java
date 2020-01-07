import java.util.*;

public class SubsetsLC78 {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        
        helper(nums, new ArrayList<Integer>(), result, 0);
        
        return result;            
    }
    
    
    public void helper(int[] nums, List<Integer> arr, List<List<Integer>> result, int pos){
        result.add(new ArrayList<Integer>(arr));
        for(int i=pos; i<nums.length; i++) {
            arr.add(nums[i]);
            helper(nums, arr, result, i+1);
            arr.remove(arr.size()-1);
        }
    }
}