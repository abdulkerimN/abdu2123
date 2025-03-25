class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        invalid_chars = [char for char in freq if freq[char] < k]
        
        if not invalid_chars:
            return len(s)
        
        max_len = 0
        start = 0
        for i, char in enumerate(s):
            if char in invalid_chars:
                substring = s[start:i]
                max_len = max(max_len, self.longestSubstring(substring, k))
                start = i + 1
        
        substring = s[start:]
        max_len = max(max_len, self.longestSubstring(substring, k))
        
        return max_len