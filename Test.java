import java.util.*;

public class Test {
    
    public static void main(String[] args) {
        List<String> al = new ArrayList<String>();

        al.add("Hello");
        al.add("Wassup");
        String listString = String.join("", al);
        System.out.println(listString);
    }
}