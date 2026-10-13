
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        original_number = x
        reversed_number = 0

        # Reverse the number
        while x > 0:
            last_digit = x % 10

            reversed_number = reversed_number * 10 + last_digit

            x //= 10

        # Compare the reversed number with the original
        return original_number == reversed_number
