class Solution:
    def generateParenthesis(self, n: int):
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: if we've used n opening and n closing parentheses
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Add an opening parenthesis if we can
            if open_count < n:
                backtrack(current_string + '(', open_count + 1, close_count)
            
            # Add a closing parenthesis if we can
            if close_count < open_count:
                backtrack(current_string + ')', open_count, close_count + 1)
        
        # Start the backtracking process
        backtrack("", 0, 0)
        
        return result
