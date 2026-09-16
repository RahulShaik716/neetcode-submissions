class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s,open_,close):
            if len(s) == 2*n:
                res.append(s)
                return 
            if open_ < n:
                dfs(s+'(',open_+1,close)
            
            if close<open_:
                dfs(s+')',open_,close+1)
        
        dfs('',0,0)
        return res
        