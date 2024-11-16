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
    def inorderTraversal(self, root: TreeNode):
        result = []
        
        # Helper function to perform the recursive traversal
        def inorder(node):
            if node is None:
                return
            inorder(node.left)  # Traverse the left subtree
            result.append(node.val)  # Visit the root
            inorder(node.right)  # Traverse the right subtree
        
        inorder(root)
        return result
