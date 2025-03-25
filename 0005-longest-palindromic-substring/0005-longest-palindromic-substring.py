class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]  # Return the longest palindrome found

        longest = ""
        for i in range(len(s)):
            # Check both odd and even length palindromes
            longest = max(longest, expand(i, i), expand(i, i + 1), key=len)
        
        return longest
