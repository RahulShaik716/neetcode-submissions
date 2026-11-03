class Solution:
    def encode(self, strs: List[str]) -> str:
    #     if not strs:
    #         return ""
    #     sizes = []
    #     res = []
    #     for s in strs:
    #         sizes.append(len(s))
        
    #     for size in sizes:
    #         res.append(str(size))
    #         res.append(",")
    #     res.append("#")
    #     res.extend(strs)
    #     return "".join(res)
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
    #     if not s:
    #         return []
    #     sizes,res,i = [],[],0
    #     while s[i]!="#":
    #         j = i 
    #         while s[j]!=",":
    #             j+=1
    #         sizes.append(int(s[i:j]))
    #         i = j + 1
    #     #increment i by 1. 
    #     i+=1
    #     for sz in sizes:
    #         res.append(s[i:i+sz])
    #         i+=sz
    #     return res
        if not s:
            return []
        i = 0
        res = [] 
        while i<len(s):
            j = i 
            while j < len(s) and s[j]!='#':
                j+=1
            l = int(s[i:j])
            res.append(s[j+1:j+l+1])
            i = j + l + 1
        return res

    
