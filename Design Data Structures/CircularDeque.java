public class CircularDeque {

    int arr[];
    int front;
    int rear;
    int size;
        
    /** Initialize your data structure here. Set the size of the deque to be k. */
    public CircularDeque(int k) {
        rear = -1;
        front = -1;
        size = k;
        arr = new int[k];
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    public boolean insertFront(int value) {
        if(isFull()) return false;
        if (rear == -1){
            rear = size-1;
            front = size-1;
        }
        else if (front==0){
            front = size-1;
        }
        else {
            front--;
        }
        arr[front] = value;
        return true;
    }
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    public boolean insertLast(int value) {
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
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    public boolean deleteFront() {
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
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    public boolean deleteLast() {
        if (isEmpty()) return false;
        arr[rear] = 0;
        if (front == rear){
            rear = -1;
            front = -1;
        }
        else if (rear==0){
            rear = size-1;
        }
        else{
            rear = rear-1;
        }
        return true;
    }
    
    /** Get the front item from the deque. */
    public int getFront() {
        if (isEmpty()) return -1;
        return arr[front];
    }
    
    /** Get the last item from the deque. */
    public int getRear() {
        if (isEmpty()) return -1;
        return arr[rear];
    }
    
    /** Checks whether the circular deque is empty or not. */
    public boolean isEmpty() {
        return rear==-1;
    }
    
    /** Checks whether the circular deque is full or not. */
    public boolean isFull() {
        return (rear==front-1) || (rear-front==size-1);
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */