class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input : list of nums, #output : list of top k frequent elements. 
        # count = {}

        # for i in nums:
        #     count[i] = count.get(i,0) + 1 #O(n)

        # arr = []
        # for value,cnt in count.items():
        #     arr.append([cnt,value])          #O(n)
                                              
        # arr.sort(reverse=True)
        #                                 O(nlogn)
        # output = []
        # for i in arr:
        #     output.append(i[1])
        #     if len(output) == k:
        #         break
        
        # return output
        # time - 3O(n) + O(nlogn) -> O(nlogn) , space - O(3n)
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        heap = []
        for value,cnt in count.items():
            heapq.heappush(heap,(cnt,value))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]
 
        