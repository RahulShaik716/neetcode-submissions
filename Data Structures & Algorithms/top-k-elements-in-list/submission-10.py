class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        freq = {}

        res = []
        for i in nums:
            count[i] = 1 + count.get(i,0)
        

        
        for value in count:
            if count[value] not in freq:
                freq[count[value]] = []
            freq[count[value]].append(value)
       
        for j in range(len(nums),-1,-1):
            if j in freq:
                for i in freq[j]:
                    res.append(i)
                    if len(res)==k:
                        return res