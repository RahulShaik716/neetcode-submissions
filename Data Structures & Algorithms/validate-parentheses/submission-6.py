class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        for c in s:
            if c in map:
                stack.append(c)
            else:
                if stack:
                    ch = stack.pop()
                    if ch not in map or map[ch]!=c:
                        return False
                else:
                    stack.append(c)
            
        return  False if len(stack) else True
        