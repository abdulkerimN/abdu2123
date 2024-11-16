class Solution:
    def generate(self, numRows: int):
        # Initialize the Pascal's triangle with the first row.
        triangle = [[1]]
        
        for row_num in range(1, numRows):
            # Start each row with the number 1
            row = [1]
            
            # Fill the middle elements by summing elements from the previous row
            for i in range(1, row_num):
                row.append(triangle[row_num - 1][i - 1] + triangle[row_num - 1][i])
            
            # End each row with the number 1
            row.append(1)
            
            # Append the row to the triangle
            triangle.append(row)
        
        return triangle
      