class Solution:
    def isValid(self, s: str) -> bool:
        #input : string, output : boolean 

        #naive - i don't know how ? 
        #best approach - using stack 
        map_ = {')':'(','}':'{',']':'['}
        stack = []
        
        for i in s:
            if i in map_:
               if stack and stack[-1] == map_[i]:
                    stack.pop()
               else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False
            


        