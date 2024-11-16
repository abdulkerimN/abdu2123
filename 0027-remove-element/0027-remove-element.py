class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # This repeatedly checks if val is in the nums list
        while val in nums:
            # If it is, then this line removes the first instance
            nums.remove(val)
        # This code repeats until val is no longer in the nums list