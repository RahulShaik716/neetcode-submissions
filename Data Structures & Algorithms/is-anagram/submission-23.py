class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input - two strings , 
        # return True if both contain the same amount of characters, return False if not 

        #naive . 

        #sort them if they are equal , then they are anagrams. 
        
        #edge cases if they differ in length , then they are not anagrams. 

        # if len(s)!=len(t):
        #     return False 

        # s = sorted(s) #O(nlogn)
        # t = sorted(t) #O(nlogn)

        # return s == t

        #time - O(nlogn) , space - O(1)

        #optimization - time - O(n) , space - O(n) use hashmap and character count . 

        countT = {}
        countS = {}

        if len(s) != len(t):
            return False 
        
        for i in range(len(s)):
            countT[t[i]] = 1 + countT.get(t[i],0)
            countS[s[i]] = 1 + countS.get(s[i],0)
        
        for i in countS:
            if i not in countT or countS.get(i,0) != countT.get(i,0):
                return False 
        
        return True

        
        