class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        count = {}
        max_length = 0 

        for end in range(0,len(s)):
            count[s[end]] = 1 + count.get(s[end],0)

            while count[s[end]] > 1:  
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1
            
            length = end - start + 1
            max_length = max(length,max_length)
        return max_length