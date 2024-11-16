# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        # Helper function to check if the tree is balanced and return the height
        def helper(node: TreeNode) -> (bool, int):
            # Base case: if the node is None, it's balanced with height 0
            if not node:
                return True, 0
            
            # Recursively check the left subtree
            left_balanced, left_height = helper(node.left)
            # Recursively check the right subtree
            right_balanced, right_height = helper(node.right)
            
            # The tree is balanced if the left and right subtrees are balanced
            # and the height difference is no more than 1
            if not left_balanced or not right_balanced:
                return False, 0
            if abs(left_height - right_height) > 1:
                return False, 0
            
            # Return whether the tree is balanced and its height
            return True, max(left_height, right_height) + 1
        
        # Call the helper function for the root
        balanced, _ = helper(root)
        return balanced
    