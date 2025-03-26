from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        
        # Build the next greater map using a monotonic stack
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Remaining elements in stack have no greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Construct result for nums1 based on the next_greater map
        return [next_greater[num] for num in nums1]
