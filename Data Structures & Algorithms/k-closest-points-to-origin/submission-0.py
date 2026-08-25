class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for idx,i in enumerate(points):
            x,y = i 
            distance = x*x + y*y 
            heapq.heappush(heap,(-distance,idx))

            if len(heap) > k:
                heapq.heappop(heap)
        
        print(heap)
        return [points[p[1]] for p in heap] 

        