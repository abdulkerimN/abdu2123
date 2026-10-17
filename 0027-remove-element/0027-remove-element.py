
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        keep_index = 0

        for current_index in range(len(nums)):
            if nums[current_index] != val:
                nums[keep_index] = nums[current_index]
                keep_index += 1

        return keep_index
