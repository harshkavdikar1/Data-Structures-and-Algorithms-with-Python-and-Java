import java.util.*;

class Trie {
    public Trie[] children = new Trie[26];
    public boolean item = false;
}

// Leetcode problem 211
class WordDictionary {

    Trie root = null;
    
    /** Initialize your data structure here. */
    public WordDictionary() {
        root = new Trie();
    }
    
    /** Adds a word into the data structure. */
    public void addWord(String word) {
        Trie node = root;
        for(char c:word.toCharArray()){
            if (node.children[c-'a']==null){
                node.children[c-'a'] = new Trie();
            }
            node = node.children[c-'a'];
        }
        node.item = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    // DFS approach
    public boolean search(String word) {
        return match(word, root, 0);
    }
    
    public boolean match(String word, Trie head, int pos){
        
        Trie node = head;
        
        for (int i=pos; i<word.length(); i++){
            char ch = word.charAt(i);
            if (ch!='.' && node.children[ch-'a']==null) return false;
            if (ch=='.'){
                for (Trie t:node.children){
                    if (t!=null){
                        if (match(word, t, i+1)) return true;
                    }
                }
                return false;
            }
            node = node.children[ch-'a'];
        }
        return node.item;
    }


    // Need to implement childrens as HashMap for faster execution
    public boolean searchBFS(String word) {
        ArrayList<Trie> queue = new ArrayList<Trie>();
        queue.add(root);
        for(char ch:word.toCharArray()){
            ArrayList<Trie> temp = new ArrayList<Trie>();
            for (Trie node:queue){
                if (ch!='.' && node.children[ch-'a']==null) continue;
                if (ch=='.'){
                    for(int i=0;i<26;i++){
                        if (node.children[i]!=null) temp.add(node.children[i]);
                    }
                }
                else temp.add(node.children[ch-'a']);
            }
            if (temp.size()==0) return false;
            queue = new ArrayList<Trie>(temp);
        }
        for (Trie node:queue){
            if (node.item==true) return true;
        }
        return false;
    }

}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

