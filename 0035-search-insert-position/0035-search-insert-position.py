class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p=0
        while p<len(nums):
            if nums[p]>=target:
                return p
            else:
                p+=1

        return len(nums)