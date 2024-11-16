# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Initialize the queue with the root node
        
        while queue:
            level = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()  # Dequeue the next node
                
                # Add the node's value to the current level list
                level.append(node.val)
                
                # Enqueue the left and right children of the current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the current level to the front of the result list (bottom-up)
            result.insert(0, level)
        
        return result      