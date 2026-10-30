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
        # count = {}
        # for i in nums:
        #     count[i] = count.get(i,0) + 1
        # #O(n)
        # heap = []
        # for value,cnt in count.items():
        #     heapq.heappush(heap,(cnt,value)) #logk
        #     if len(heap) > k:
        #         heapq.heappop(heap)  #O(1)
        
        # return [x[1] for x in heap]
        # #O(n) + O(nlogk) , O(n+k)

        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for value,cnt in count.items():
            freq[cnt].append(value)
        
        output = []
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                output.append(j)
                if len(output) == k:
                    return output
         