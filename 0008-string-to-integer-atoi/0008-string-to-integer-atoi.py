
class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        string_length = len(s)

        # 1. Skip leading spaces
        while index < string_length and s[index] == " ":
            index += 1

        # 2. Check the sign
        sign = 1

        if index < string_length and s[index] == "-":
            sign = -1
            index += 1
        elif index < string_length and s[index] == "+":
            index += 1

        # 3. Read digits and build the number
        number = 0

        while index < string_length and s[index].isdigit():
            digit = int(s[index])
            number = number * 10 + digit
            index += 1

        # 4. Apply the sign
        number *= sign

        # 5. Clamp to the 32-bit signed integer range
        minimum_integer = -(2**31)
        maximum_integer = 2**31 - 1

        if number < minimum_integer:
            return minimum_integer

        if number > maximum_integer:
            return maximum_integer

        return number
