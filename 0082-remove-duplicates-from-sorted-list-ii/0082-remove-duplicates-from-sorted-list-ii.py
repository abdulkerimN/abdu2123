# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Duplicate found, skip all nodes with this value
                duplicate_value = current.val
                while current and current.val == duplicate_value:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next
                
        return dummy.next