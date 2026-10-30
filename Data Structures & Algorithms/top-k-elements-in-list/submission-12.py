class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input : list of nums, #output : list of top k frequent elements. 
        count = {}

        for i in nums:
            count[i] = count.get(i,0) + 1

        arr = []
        for value,cnt in count.items():
            arr.append([cnt,value])
        
        arr.sort(reverse=True)

        output = []
        for i in arr:
            output.append(i[1])
            if len(output) == k:
                break
        
        return output

        