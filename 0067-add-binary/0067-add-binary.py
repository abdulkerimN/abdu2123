class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize pointers for both strings and the carry
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        # Iterate until we've processed both strings and the carry
        while i >= 0 or j >= 0 or carry:
            # Take the current bits of a and b, defaulting to '0' if out of bounds
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum of the bits plus any carry
            total = bit_a + bit_b + carry
            
            # The new bit for the result is the total modulo 2
            result.append(str(total % 2))
            
            # Update carry (1 if total >= 2, else 0)
            carry = total // 2
            
            # Move to the next bits
            i -= 1
            j -= 1
        
        # The result list contains the bits in reverse order, so reverse it before joining
        return ''.join(reversed(result))

