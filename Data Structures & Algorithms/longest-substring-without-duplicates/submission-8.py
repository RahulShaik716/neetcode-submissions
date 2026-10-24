class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input : string s , output : length - int of longest substring without repeating characters. 
        #for all the substrings , check the substrings that have unique characters. 
        # def containsDuplicate(sub):
        #     hash = {}
        #     for i in sub:
        #         if i in hash:
        #             return True 
        #         hash[i] = 1
        #     return False 
        # #brute force, 
        # n = len(s)
        # res = []
        # for i in range(n):
        #     sub_str = ""
        #     for j in range(i,n):
        #         sub_str+=s[j]
        #         res.append(sub_str)
        # max_length = 0 
        # for st in res:
        #     if not containsDuplicate(st):
        #         max_length = max(max_length,len(st))
        
        # return max_length

        start = 0 
        count = {}
        max_length = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end],0) + 1
            while count[s[end]] > 1:
                count[s[start]] -= 1
                start += 1
            
            length = end - start + 1
            max_length = max(length,max_length)
        return max_length
            
        
            

        
       