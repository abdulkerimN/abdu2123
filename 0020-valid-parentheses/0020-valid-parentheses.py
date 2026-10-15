
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching_brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if not stack:
                    return False

                last_opening_bracket = stack.pop()

                if last_opening_bracket != matching_brackets[bracket]:
                    return False

        return len(stack) == 0
