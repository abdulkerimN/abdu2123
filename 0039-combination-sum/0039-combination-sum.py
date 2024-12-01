class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, target, current_combination):
            # Base case: if target is 0, we found a valid combination
            if target == 0:
                result.append(list(current_combination))
                return
            
            # If target becomes negative, we stop exploring this path
            if target < 0:
                return
            
            # Explore further with each candidate starting from 'start'
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                # We allow the same element to be used again, so we pass 'i' (not 'i + 1')
                backtrack(i, target - candidates[i], current_combination)
                # Backtrack, remove the last element
                current_combination.pop()
        
        # Start the backtracking process from index 0
        backtrack(0, target, [])
        return result
