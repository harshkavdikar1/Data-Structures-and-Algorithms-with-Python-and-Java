public class CircularQueue {
    
    private int arr[];
    private int size;
    private int front;
    private int rear;

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public CircularQueue(int k) {
        arr = new int[k];
        rear = -1;
        front = -1;
        size = k;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if(isFull()) return false;
        if (rear == -1){
            rear = 0;
            front = 0;
        }
        else{
            rear = (rear+1)%size;
        }
        arr[rear] = value;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if (isEmpty()) return false;
        arr[front] = 0;
        if (front == rear){
            rear = -1;
            front = -1;
        }
        else{
            front = (front+1)%size;
        }
        return true;
    }
    
    
    /** Get the front item from the queue. */
    public int Front() {
        if (isEmpty()) return -1;
        return arr[front];
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        if (isEmpty()) return -1;
        return arr[rear];
    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return rear==-1;
    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return (rear==front-1) || (rear-front==size-1);
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */