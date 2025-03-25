class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, i = 0, len(nums) - 1, 0

        while i <= right:
            if nums[i] == 0:  # Swap 0 to the left
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:  # Swap 2 to the right
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:  # If it's 1, just move to the next
                i += 1