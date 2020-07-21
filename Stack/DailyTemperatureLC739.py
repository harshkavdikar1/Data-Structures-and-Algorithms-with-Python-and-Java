class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for index, temp in enumerate(T):
            if not stack or T[stack[-1]] >= temp:
                stack.append(index)
            else:
                while stack and T[stack[-1]] < temp:
                    x = stack.pop()
                    ans[x] = index - x
                stack.append(index)
        return ans
