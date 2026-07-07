class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += str(len(i))+'#'+i
        print(s)
        return s


    def decode(self, s: str) -> List[str]:
        res = []
        """we take the int , loop till # and then parseInt once we encounter #
        take the next characters for that length , push it to res , 
        increment len(number)+1+number
        """
        i=0
        while i<len(s):
            n = ''
            j = i
            while s[j]!='#':
                n += s[j]
                j += 1
            length = int(n)
            res.append(s[(i+len(n)+1):(i+length+len(n)+1)])
            i += length + len(n) + 1
        return res
            


