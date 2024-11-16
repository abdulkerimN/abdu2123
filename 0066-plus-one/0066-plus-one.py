class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        right = len(digits) - 1
        while right >= 0:
            digit = digits[right] + 1
            if digit > 9:
                digits[right] = 0
                right -= 1
            else:
                digits[right] = digit
                break

        if right == -1:
            digits.insert(0, 1)
        return digits