import java.util.*;


// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
interface NestedInteger {

    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    public boolean isInteger();

    // @return the single integer that this NestedInteger holds, if it holds a single integer
    // Return null if this NestedInteger holds a nested list
    public Integer getInteger();

    // @return the nested list that this NestedInteger holds, if it holds a nested list
    // Return null if this NestedInteger holds a single integer
    public List<NestedInteger> getList();
}

public class NestedListIterator implements Iterator<Integer> {

    Queue<Integer> queue;
    
    public NestedListIterator(List<NestedInteger> nestedList) {
        ArrayList<Integer> x = new ArrayList<Integer>();
        Iterator<NestedInteger> it = nestedList.iterator();
        if(it.hasNext()) x.addAll(getList(it));
        queue = new LinkedList<Integer>(x);
    }
    
    public ArrayList<Integer> getList(Iterator<NestedInteger> it) {
        ArrayList<Integer> x = new ArrayList<Integer>();
        NestedInteger element = it.next();
        if (element.isInteger()) {
            x.add(element.getInteger());
        }
        else{
            Iterator<NestedInteger> it2 = element.getList().iterator();
            if(it2.hasNext()) x.addAll(getList(it2));
        }
        if(it.hasNext()){
            x.addAll(getList(it));    
        }
        return x;
    }

    @Override
    public Integer next() {
        return queue.remove();
    }

    @Override
    public boolean hasNext() {
        if (queue.size()>0) return true;
        return false;
    }

}

//
//   Your NestedIterator object will be instantiated and called as such:
//   NestedIterator i = new NestedIterator(nestedList);
//   while (i.hasNext()) v[f()] = i.next();
// 