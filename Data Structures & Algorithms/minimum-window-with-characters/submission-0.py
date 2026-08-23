class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t:
            return ""
        countT = {}
        for i in t:
            countT[i] = 1 + countT.get(i,0)
        
        start = 0 
        max_string = [-1,-1]
        max_length = float("inf")
        have,need = 0,len(countT)
        countS = {}
        for end in range(len(s)):
            countS[s[end]] = 1 + countS.get(s[end],0)
            c= s[end]

            if c in countT and countS[c] == countT[c]:
                have += 1
            
            while have == need:
                if end-start+1 < max_length:
                    max_string = [start,end]
                    max_length = end-start + 1
                
                countS[s[start]] -= 1
                if s[start] in countT and countS[s[start]] < countT[s[start]]:
                    have -= 1
                start += 1
        
        start,end = max_string

        return s[start:end+1] if max_length!=float("inf") else ""

            

        
        