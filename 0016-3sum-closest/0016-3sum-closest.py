class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If the sum is exactly the target, return immediately
                if current_sum == target:
                    return current_sum

                # Update the closest sum if found a better one
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move pointers based on sum comparison
                if current_sum < target:
                    left += 1  # Increase sum
                else:
                    right -= 1  # Decrease sum

        return closest_sum