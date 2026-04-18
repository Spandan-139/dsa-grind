class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        current = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first = current
        mid = slow
        second = slow.next
        slow.next = None
        prev = None
        curr = second

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        second = prev
        while first and second:
            next1 = first.next
            next2 = second.next
            first.next = second
            second.next = next1
            first = next1
            second = next2
