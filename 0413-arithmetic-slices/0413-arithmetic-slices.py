class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        total = 0
        current_diff = nums[1] - nums[0]
        count = 2  # at least two elements to start forming a potential arithmetic sequence
        
        for i in range(2, len(nums)):
            new_diff = nums[i] - nums[i-1]
            if new_diff == current_diff:
                count += 1
            else:
                if count >= 3:
                    total += (count - 1) * (count - 2) // 2
                current_diff = new_diff
                count = 2
        
        # Add the last segment if it's long enough
        if count >= 3:
            total += (count - 1) * (count - 2) // 2
        
        return total