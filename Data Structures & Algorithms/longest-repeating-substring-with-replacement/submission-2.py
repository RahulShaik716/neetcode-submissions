class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0 
        count = {}
       
        max_freq = 0
        res = 0
        for end in range(0,len(s)):
            count[s[end]] = 1 + count.get(s[end],0)
            max_freq = max(count[s[end]],max_freq)
            while (end-start+1) - max_freq > k:
                count[s[start]] -= 1
                start+=1
            res = max(res, end - start + 1 )
        return res