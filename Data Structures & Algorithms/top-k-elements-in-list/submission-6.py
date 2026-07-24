class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = defaultdict(list)
        for i in nums:
            count[i] = 1+count.get(i,0)
        
        for i in count:
            freq[count[i]].append(i)
        
        res = []

        for i in range(len(nums),0,-1):
            if freq[i]:
                for j in freq[i]:
                    res.append(j)
                    if len(res)==k:
                        return res
