class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        for i in s1:
            counts1[i] = counts1.get(i,0) + 1 
        
        counts2 = {}
        start = 0 
        k = len(s1)
        for end in range(len(s2)):
            counts2[s2[end]] = 1 + counts2.get(s2[end],0)
            if end-start + 1 == k:
                if counts1 == counts2:
                    return True 
                else:
                    counts2[s2[start]] -= 1
                    if counts2[s2[start]] == 0:
                        del counts2[s2[start]]
                    start +=1
        return False