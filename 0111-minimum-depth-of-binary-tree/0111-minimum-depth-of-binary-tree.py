# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # If left subtree is None, return depth of right subtree + 1
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # If right subtree is None, return depth of left subtree + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # Both subtrees are non-empty, so we compute the minimum depth
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        return min(left_depth, right_depth) + 1
   