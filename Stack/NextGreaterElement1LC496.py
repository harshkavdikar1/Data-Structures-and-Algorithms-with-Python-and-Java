class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        if not nums2:
            return [-1] * len(nums1)
        d = {}
        stack = []
        result = []
        for num in nums2:
            while stack and stack[-1] < num:
                d[stack.pop()] = num
            stack.append(num)
        return [d.get(num, -1) for num in nums1]
