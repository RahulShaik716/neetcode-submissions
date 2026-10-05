class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = s.lower()
        ct = re.sub(r'[^a-zA-Z0-9]', '', st)
        left = 0 
        right = len(ct)-1
        while left<right:
            print(st[left],st[right])
            if ct[left]!=ct[right]:
                return False
            left+=1
            right-=1
        
        return True
        