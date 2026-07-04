class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashM = {}
        for i in nums:
            hashM[i] = 1 + hashM.get(i,0)
        
        #sort based on keys 
        s = sorted(hashM, key = lambda x:hashM[x],reverse=True)
        return s[:k]