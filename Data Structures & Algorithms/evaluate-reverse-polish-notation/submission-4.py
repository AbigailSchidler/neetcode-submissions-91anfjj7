class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # while an operator is not found
            # add to stack
        # pop everything from stack and combine with operator
        # add result back to stack
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token in operators:
                second = stack.pop()
                first = stack.pop()
                res = self.combine(first, second, token)
                print(res)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()
    
    def combine(self, first: int, second: int, token: str) -> int:
        if token == '+':
            return first + second
        elif token == '-':
            return first - second
        elif token == '*':
            return first * second
        else:
            return int(first / second)