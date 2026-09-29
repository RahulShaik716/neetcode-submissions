class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)

        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            n = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-n)

        if len(self.max_heap) > len(self.min_heap) + 1:
            n = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-n)


        if len(self.min_heap) > len(self.max_heap) + 1:
            n = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-n)
    

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap): 
            return -self.max_heap[0]
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return (-self.max_heap[0] + self.min_heap[0])/2    
        