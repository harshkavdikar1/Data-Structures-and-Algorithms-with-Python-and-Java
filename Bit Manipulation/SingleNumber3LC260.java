public class SingleNumber3LC260 {

    public int[] singleNumber(int[] nums) {
        int result = 0;

        for (int num : nums){
            result ^= num;
        }

        int counter = 0;
        while (result%2==0){
            result /= 2;
            counter++;
        }

        int first=0;
        int second=0;

        for (int num : nums){
            if ((num>>counter)%2==0) first ^= num;
            else second ^= num;
        }

        return new int[] {first, second};        
    }
}