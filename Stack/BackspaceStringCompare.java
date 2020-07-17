import java.util.*;

/**
 * LeetCode Problem 844
 */
public class BackspaceStringCompare {

    // O(N) time and O(1) Space
    public boolean backspaceCompare(String S, String T) {
        int s = S.length() - 1;
        int t = T.length() - 1;
        int c;
        while (s > -1 || t > -1) {
            c = 0;
            while (s > -1 && (c > 0 || S.charAt(s) == '#')) {
                if (S.charAt(s) == '#')
                    c++;
                else if (c > 0)
                    c--;
                s--;
            }
            c = 0;
            while (t > -1 && (c > 0 || T.charAt(t) == '#')) {
                if (T.charAt(t) == '#')
                    c++;
                else if (c > 0)
                    c--;
                else
                    break;
                t--;
            }

            if (s > -1 && t > -1 && S.charAt(s) == T.charAt(t)) {
                s--;
                t--;
            } else
                break;
        }
        return s <= -1 && t <= -1;
    }

    // O(N) Space O(N) Time
    public boolean backspaceCompareWithStack(String S, String T) {
        Stack<Character> s = new Stack<>();
        Stack<Character> t = new Stack<>();

        for (int i = 0; i < S.length(); i++) {
            char ch = S.charAt(i);
            if (ch == '#') {
                if (s.size() > 0)
                    s.pop();
            } else
                s.push(ch);
        }
        for (int i = 0; i < T.length(); i++) {
            char ch = T.charAt(i);
            if (ch == '#') {
                if (t.size() > 0)
                    t.pop();
            } else
                t.push(ch);
        }
        return s.equals(t);
    }
}
