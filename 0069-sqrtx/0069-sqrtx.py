class Solution:
    def mySqrt(self, x: int) -> int:
        # Special cases for 0 and 1
        if x == 0 or x == 1:
            return x
        
        # Initialize binary search bounds
        left, right = 0, x
        
        # Binary search to find the integer part of the square root
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid  # Found exact square root
            elif mid * mid < x:
                left = mid + 1  # Increase search range
            else:
                right = mid - 1  # Decrease search range
        
        # At the end of the loop, right will be the floor of the square root
        return right
