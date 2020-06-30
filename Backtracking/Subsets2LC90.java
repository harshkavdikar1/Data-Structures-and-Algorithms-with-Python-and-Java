import java.util.*;

public class Subsets2LC90 {
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        
        Arrays.sort(nums);
        helper(nums, new ArrayList<Integer>(), new Boolean[nums.length], result, 0);
        
        return result;
    }
    
    public void helper(int[] nums, List<Integer> arr, Boolean[] used, List<List<Integer>> result, int pos){
        result.add(new ArrayList<Integer>(arr));
        for(int i=pos; i<nums.length; i++) {
            if (i>0 && !used[i-1] && nums[i] == nums[i-1]) continue;
            arr.add(nums[i]);
            used[i] = true;
            helper(nums, arr,used, result, i+1);
            arr.remove(arr.size()-1);
            used[i] = false;
        }
    }
}