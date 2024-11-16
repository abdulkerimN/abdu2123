# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Helper function to compare two trees
        def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
            # Base cases
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            # Check if the current nodes are symmetric
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        # A tree is symmetric if the left and right subtrees are mirrors of each other
        if not root:
            return True
        return isMirror(root.left, root.right)
