class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge case for overflow condition
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        sign = 1
        if (dividend < 0) != (divisor < 0):  # if the signs of dividend and divisor are different
            sign = -1
        
        # Work with positive values to simplify the process
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # Keep subtracting divisor * (2^k) until dividend is smaller than divisor
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  # Double the divisor
                temp <<= 1
                multiple <<= 1
            
            # Subtract the largest possible multiple of divisor
            dividend -= temp
            quotient += multiple
        
        # Apply the sign to the quotient
        return sign * quotient
