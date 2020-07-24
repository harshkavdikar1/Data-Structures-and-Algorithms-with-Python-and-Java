class ValidParantheses:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "}": "{", "]": "["}
        stack = []
        for ch in s:
            if ch in d:
                if not stack or stack.pop() != d[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
