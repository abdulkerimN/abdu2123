class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []  # Stack to store result characters
        seen = set()  # Set to check if a character is in the stack
        last_occurrence = {char: idx for idx, char in enumerate(s)}  # Last occurrence index of each character
        
        for idx, char in enumerate(s):
            if char not in seen:
                # Ensure lexicographical order by removing larger characters if they appear later
                while stack and char < stack[-1] and last_occurrence[stack[-1]] > idx:
                    seen.remove(stack.pop())
                
                stack.append(char)
                seen.add(char)
        
        return ''.join(stack)
