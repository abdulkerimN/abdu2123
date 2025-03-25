class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Compute the effective rotation
        k %= length
        if k == 0:
            return head

        # Step 3: Find the new tail (length - k - 1)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Step 4: Re-arrange pointers
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head  # Connect old tail to old head

        return new_head