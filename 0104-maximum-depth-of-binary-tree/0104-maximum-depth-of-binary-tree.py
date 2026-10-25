# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        # If the tree is empty, its depth is 0
        if root is None:
            return 0

        # Find the depth of the left subtree
        left_depth = self.maxDepth(root.left)

        # Find the depth of the right subtree
        right_depth = self.maxDepth(root.right)

        # Return the larger depth plus the current node
        return 1 + max(left_depth, right_depth)
