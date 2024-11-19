class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        ans = 0
        h = len(height) - 1
        
        while l < h:
            # Calculate the area between the lines at indices l and h.
            a = min(height[l], height[h]) * (h - l)
            # Update ans with the maximum of the current area and the existing maximum.
            ans = max(a, ans)
            
            # Move the pointer that points to the shorter line inward.
            # Moving the pointer pointing to the taller line won't increase the area.
            if height[l] < height[h]:
                l += 1
            else:
                h -= 1
        
        return ans