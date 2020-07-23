# LC 1047
class Solution:
    # Two pointer
    def removeDuplicates(self, S: str) -> str:
        res = [0] * len(S)
        i = -1
        for j, ch in enumerate(S):
            if i >= 0 and res[i] == ch:
                i -= 1
            else:
                i += 1
                res[i] = ch
        return ''.join(res[:i+1])

    # Stack Approach

    def removeDuplicatesStack(self, S: str) -> str:
        stack = []
        for ch in S:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
