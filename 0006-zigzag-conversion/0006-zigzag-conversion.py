
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        moving_down = True

        for character in s:
            rows[current_row] += character

            if current_row == 0:
                moving_down = True
            elif current_row == numRows - 1:
                moving_down = False

            if moving_down:
                current_row += 1
            else:
                current_row -= 1

        return "".join(rows)
