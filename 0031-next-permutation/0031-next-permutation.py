class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        
        # Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find the next larger element and swap
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the right part
        nums[i + 1:] = reversed(nums[i + 1:])