from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to store the frequency of each character
        frequency = defaultdict(int)
        for char in s:
            frequency[char] += 1
        
        # Iterate through the string to find the first character with frequency 1
        for index, char in enumerate(s):
            if frequency[char] == 1:
                return index
        
        # If no such character found, return -1
        return -1