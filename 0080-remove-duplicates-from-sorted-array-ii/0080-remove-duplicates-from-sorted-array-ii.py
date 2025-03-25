class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # If length is 2 or less, no changes are needed

        index = 2  # Start from the third position

        for i in range(2, len(nums)):
            if nums[i] != nums[index - 2]:  # Allow only up to two occurrences
                nums[index] = nums[i]
                index += 1

        return index