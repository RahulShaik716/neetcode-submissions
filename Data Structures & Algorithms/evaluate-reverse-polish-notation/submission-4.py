class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+*-/'
        for i in tokens:
            if i in operators:
                op2 = int(stack.pop())
                op1 = int(stack.pop())

                match i:
                    case '+':
                        stack.append(op2+op1)
                    case '-':
                        stack.append(op1-op2)
                    case '*':
                        stack.append(op1*op2)
                    case '/':
                        stack.append(int(float(op1)/op2))
            else:
                stack.append(int(i))
        
        return stack[0]

                