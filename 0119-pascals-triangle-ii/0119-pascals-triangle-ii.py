
class Solution:
    def getRow(self, rowIndex: int):
        # Initialize the row as an array with a single element [1]
        row = [1] * (rowIndex + 1)
        
        # Compute each element in the row using the iterative binomial coefficient formula
        for k in range(1, rowIndex + 1):
            # Update each element in reverse order to ensure we use the previous element
            row[k] = row[k - 1] * (rowIndex - k + 1) // k
        
        return row
      