class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):
            length1 = expand(i, i)
            length2 = expand(i, i + 1)

            length = max(length1, length2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]