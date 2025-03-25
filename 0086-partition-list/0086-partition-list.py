# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Initialize two dummy nodes to serve as the heads of the before and after lists
        before_head = ListNode(0)
        after_head = ListNode(0)
        # Pointers to the current end of the before and after lists
        before = before_head
        after = after_head
        
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        
        # Connect the before list to the after list
        before.next = after_head.next
        # Ensure the after list ends properly
        after.next = None
        
        return before_head.next