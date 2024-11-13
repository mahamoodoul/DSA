from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        sign = ["+", "-","/", "*"]
        result= 0
        for token in tokens:
            if token not in  sign:
                stack.append(token)
            else:
                if stack:
                    val = int(stack.pop())
                    val1 = int(stack.pop())
                    if token == '+':
                        result = val1 + val
                    elif token == '-':
                        result = val1 - val
                    elif token == '*':
                        result = val1 * val
                    elif token == '/':
                        result = val1 / val
                    else:
                        result = "Invalid token"
                    stack.append(result)
        return int(result)




tokens = ["18"]
obj = Solution()
output = obj.evalRPN(tokens)
print(output)