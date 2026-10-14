
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for index in range(len(s)):
            current_value = roman_values[s[index]]

            if index + 1 < len(s) and current_value < roman_values[s[index + 1]]:
                total -= current_value
            else:
                total += current_value

        return total
