class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        
        res = [-heap[0][0]]

        for end in range(k,len(nums)):
            heapq.heappush(heap,(-nums[end],end))
            start = end-k+1
            while heap[0][1] < start:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res
        
        