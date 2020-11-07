import java.util.*;

public class MedianDataStreamLC295 {
    Queue<Integer> large;
    Queue<Integer> small;

    /** initialize your data structure here. */
    public MedianDataStreamLC295() {
        large = new PriorityQueue<Integer>();
        small = new PriorityQueue<Integer>();
    }
    
    public void addNum(int num) {
        large.add(num);
        small.add(-large.poll());
        if (small.size() > large.size()) {
            large.add(-small.poll());
        }
    }
    
    public double findMedian() {
        return large.size() > small.size()
               ? large.peek()
               : (large.peek() - small.peek()) / 2.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */