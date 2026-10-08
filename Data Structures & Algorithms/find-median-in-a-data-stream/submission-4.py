class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-num)

        #cases would be diff b/w max and min > 1 and maxHeap[0] > minHeap[0] , push it to minHeap and 

        if self.minHeap and self.minHeap[0] < -self.maxHeap[0]:
            n = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,-n)
        
        if len(self.maxHeap) > len(self.minHeap) + 1 : 
            n = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,-n)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            n = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-n)

    def findMedian(self) -> float:
        if len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        if len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        
        return (self.minHeap[0] + -self.maxHeap[0])/2 
        
        