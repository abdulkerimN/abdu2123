# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        # If the tree is empty, no path exists
        if root is None:
            return False

        # Subtract the current node's value
        targetSum -= root.val

        # Check whether this is a leaf
        if root.left is None and root.right is None:
            return targetSum == 0

        # Check the left path or the right path
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))
       