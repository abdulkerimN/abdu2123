from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []  # This will store pairs (num, min_left)
        min_left = nums[0]
        
        for j in range(1, len(nums)):
            while stack and nums[j] >= stack[-1][0]:
                stack.pop()
            
            if stack and nums[j] > stack[-1][1]:
                return True
            
            stack.append((nums[j], min_left))
            min_left = min(min_left, nums[j])
        
        return False
