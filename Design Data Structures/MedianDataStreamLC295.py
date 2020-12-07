from heapq import heappush, heappushpop, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        small, large = self.minHeap, self.maxHeap
        
        heappush(small, -heappushpop(large, -num))
        if len(small) > len(large):
            heappush(large, -heappop(small))        

    def findMedian(self) -> float:
        small, large = self.minHeap, self.maxHeap
        if (len(small) + len(large))%2 == 0:
            return (-float(large[0]) + float(small[0]))/2
        return -float(large[0])
            
 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()