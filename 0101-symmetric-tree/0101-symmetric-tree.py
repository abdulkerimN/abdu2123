# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            # If both nodes are empty, they match
            if left is None and right is None:
                return True

            # If only one node is empty, they don't match
            if left is None or right is None:
                return False

            # Their values must be equal
            if left.val != right.val:
                return False

            # Compare opposite sides like a mirror
            return (isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))

        return isMirror(root.left, root.right) if root else True
     