# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        mid = slow.next
        slow.next = None
        
        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge the sorted halves
        dummy = ListNode(0)
        current = dummy
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        current.next = left if left else right
        
        return dummy.next