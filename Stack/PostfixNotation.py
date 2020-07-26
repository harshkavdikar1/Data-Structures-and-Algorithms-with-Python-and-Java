class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "*/+-":
                stack.append(int(token))
            else:
                if not stack:
                    return 0
                y = stack.pop()
                if not stack:
                    return 0
                x = stack.pop()
                if token == "-":
                    stack.append(x-y)
                elif token == "+":
                    stack.append(x+y)
                elif token == "*":
                    stack.append(x*y)
                elif token == "/":
                    stack.append(int(x/y))
        return stack[-1]
