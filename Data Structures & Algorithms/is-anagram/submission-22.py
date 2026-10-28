class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input - two strings , 
        # return True if both contain the same amount of characters, return False if not 

        #naive . 

        #sort them if they are equal , then they are anagrams. 
        
        #edge cases if they differ in length , then they are not anagrams. 

        if len(s)!=len(t):
            return False 

        s = sorted(s)
        t = sorted(t)

        return s == t
        