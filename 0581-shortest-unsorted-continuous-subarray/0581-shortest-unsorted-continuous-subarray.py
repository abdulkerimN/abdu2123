from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = next((i for i in range(len(nums)) if nums[i] != sorted_nums[i]), len(nums)), next((i for i in range(len(nums) - 1, -1, -1) if nums[i] != sorted_nums[i]), -1)
        return max(0, right - left + 1)
