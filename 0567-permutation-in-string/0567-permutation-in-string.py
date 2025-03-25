from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        
        for char in s1:
            s1_count[char] += 1
        
        for i in range(len(s2)):
            s2_count[s2[i]] += 1
            
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                if s2_count[left_char] == 1:
                    del s2_count[left_char]
                else:
                    s2_count[left_char] -= 1
            
            if s2_count == s1_count:
                return True
        
        return False