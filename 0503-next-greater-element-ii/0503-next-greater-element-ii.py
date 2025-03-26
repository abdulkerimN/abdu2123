from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  # Default to -1 for elements with no greater element
        stack = []  # Monotonic decreasing stack to keep indices
        
        # Iterate twice to simulate circular array
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                result[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        
        return result
