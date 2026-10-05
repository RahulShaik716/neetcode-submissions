class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}' : '{', ')':'(',']' : '['}
        stack = []

        for i in s:
            if i not in map:
                stack.append(i)
            else:
                if stack:
                    n = stack.pop()
                    if n!=map[i]:
                        return False
                else:
                    return False
                
        return True if len(stack) == 0 else False