import java.util.*;

class Permutation2 {
    public List<List<Integer>> permuteUnique(int[] nums) {
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        
        List<Boolean> used = new ArrayList<Boolean>();
        
        for (int i=0;i<nums.length;i++){
            used.add(false);
        }
        
        Arrays.sort(nums);
        
        helper(nums, used, new ArrayList<Integer>(), result);
        
        return result;
    }

    public void helper(int[] nums, List<Boolean> used, List<Integer> arr, List<List<Integer>> result){
        if (nums.length==arr.size()) result.add(new ArrayList<Integer>(arr));
        else {
            for(int i=0; i<nums.length; i++){
                if(used.get(i)==true || (i>0 && !used.get(i - 1) && nums[i-1]==nums[i])) continue;
                used.set(i,true);
                arr.add(nums[i]);
                helper(nums, used, arr, result);
                arr.remove(arr.size()-1);
                used.set(i,false);
            }
        }
    }
}


public class Permutations2LC46 {
    public static void main(String[] args) {
        Permutation2 perm = new Permutation2();

        int nums[] = {1,1,2,3};

        System.out.println(perm.permuteUnique(nums));
    }
}