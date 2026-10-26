class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_ = min(val,self.min_stack[-1] if self.min_stack else val)
        #pushing min of val and  min into min_stack , it would definitely have duplicates 
        self.min_stack.append(min_)


    def pop(self) -> None:
        self.stack.pop()
        #stack.pop() , min_stack.pop() might be different why does it work ? 
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        #should return the minimum element in the stack and should be in O(1) time
        return self.min_stack[-1]
