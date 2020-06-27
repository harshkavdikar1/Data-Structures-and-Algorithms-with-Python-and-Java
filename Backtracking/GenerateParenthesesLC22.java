
import java.util.*;

public class GenerateParenthesesLC22 {
    public List<String> generateParenthesis(int n) {
        
        List<String> result = new ArrayList<String>();
        
        helper(n, n, result, new ArrayList<String>());
        
        return result;
    }
    
    public void helper(int open, int close, List<String> result, List<String> arr){
        if(open==close && open==0) result.add(String.join("",arr));
        
        if(open>0){
            arr.add("(");
            helper(open-1, close, result, arr);
            arr.remove(arr.size()-1);
        }        
        if(close>open){
            arr.add(")");
            helper(open, close-1, result, arr);
            arr.remove(arr.size()-1);
        }
    }

    public static void main(String[] args) {
        GenerateParenthesesLC22 gp = new GenerateParenthesesLC22();
        System.out.println(gp.generateParenthesis(3));
    }
}