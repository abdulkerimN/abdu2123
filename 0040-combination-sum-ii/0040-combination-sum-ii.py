class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        
        # Sort the candidates to facilitate skipping duplicates
        candidates.sort()

        def backtrack(start, target, current_combination):
            # If the target is zero, we found a valid combination
            if target == 0:
                result.append(list(current_combination))
                return

            # Try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                # Skip duplicates: if the current number is the same as the previous one, skip it
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If the candidate exceeds the remaining target, break (as the list is sorted)
                if candidates[i] > target:
                    break
                
                # Choose the current candidate and move forward
                current_combination.append(candidates[i])
                # Recurse with the next number (i + 1), because each number can be used only once
                backtrack(i + 1, target - candidates[i], current_combination)
                # Backtrack: remove the last candidate
                current_combination.pop()
        
        # Start the backtracking process
        backtrack(0, target, [])
        
        return result
