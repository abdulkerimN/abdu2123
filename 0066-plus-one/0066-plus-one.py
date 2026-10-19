
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        last_index = len(digits) - 1

        for index in range(last_index, -1, -1):
            if digits[index] < 9:
                digits[index] += 1
                return digits

            digits[index] = 0

        digits.insert(0, 1)
        return digits
