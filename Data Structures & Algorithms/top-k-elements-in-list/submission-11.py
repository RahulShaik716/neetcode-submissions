class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for value in count:
            if count[value] not in freq:
                freq[count[value]] = []
            freq[count[value]].append(value) 
        res = []
        for i in range(len(nums),-1,-1):
            if i in freq:
                for j in freq[i]:
                    res.append(j)
                    if len(res) == k:
                        return res
        