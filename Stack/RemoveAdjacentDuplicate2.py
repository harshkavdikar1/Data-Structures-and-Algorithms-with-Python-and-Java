# Leetcode Problem 1209
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return "".join([x*y for x, y in stack])
