# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        # If both trees are empty, they are the same
        if p is None and q is None:
            return True

        # If only one tree is empty, they are different
        if p is None or q is None:
            return False

        # If the current values are different, trees are different
        if p.val != q.val:
            return False

        # Compare the left children and right children
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
